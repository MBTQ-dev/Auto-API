"""
MBTQ Auto-API - FastAPI Backend
================================
Main FastAPI application for the MBTQ API Autopilot system.
Integrates with DeafAUTH, Fibonrose, and PinkSync services.
"""

from fastapi import FastAPI, HTTPException, Depends, Header
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from typing import Optional, List, Dict, Any
from datetime import datetime, timedelta
import httpx
import logging

from models import (
    APIEntry, 
    APIFilter, 
    CodeGenerationRequest, 
    CodeGenerationResponse,
    DeploymentRequest,
    DeploymentResponse,
    AuthRequest,
    AuthResponse,
    FibonroseLog
)
from services.deafauth import DeafAuthService
from services.fibonrose import FibonroseService
from services.pinksync import PinkSyncService
from services.code_generator import CodeGeneratorService
from services.curated_apis import CuratedAPIsService

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="MBTQ Auto-API",
    description="Visual-first API integration with auto-deployment to mbtq.dev",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify actual origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
deafauth_service = DeafAuthService()
fibonrose_service = FibonroseService()
pinksync_service = PinkSyncService()
code_generator_service = CodeGeneratorService()
curated_apis_service = CuratedAPIsService()

# Dependency for authentication
async def verify_auth(x_mbtq_token: Optional[str] = Header(None)) -> dict:
    """Verify DeafAUTH token and return user info"""
    if not x_mbtq_token:
        raise HTTPException(status_code=401, detail="DeafAUTH token required")
    
    user = await deafauth_service.verify_token(x_mbtq_token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid DeafAUTH token")
    
    return user


@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "name": "MBTQ Auto-API",
        "version": "1.0.0",
        "status": "operational",
        "services": {
            "deafauth": "🔐 Active",
            "fibonrose": "🌹 Active",
            "pinksync": "⚡ Active"
        },
        "docs": "/api/docs",
        "timestamp": datetime.utcnow().isoformat()
    }


@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "services": {
            "deafauth": await deafauth_service.health_check(),
            "fibonrose": await fibonrose_service.health_check(),
            "pinksync": await pinksync_service.health_check(),
            "curated_apis": await curated_apis_service.health_check()
        }
    }


@app.post("/api/auth/login", response_model=AuthResponse)
async def login(auth_request: AuthRequest):
    """
    Authenticate user with DeafAUTH
    """
    try:
        # Log authentication attempt
        await fibonrose_service.log_event(
            action="auth_attempt",
            metadata={"username": auth_request.username},
            user="system"
        )
        
        # Authenticate with DeafAUTH
        result = await deafauth_service.authenticate(
            auth_request.username, 
            auth_request.password
        )
        
        if result["success"]:
            # Log successful authentication
            await fibonrose_service.log_event(
                action="auth_success",
                metadata={"username": auth_request.username},
                user=auth_request.username
            )
            
            return AuthResponse(
                success=True,
                token=result["token"],
                username=auth_request.username,
                message="DeafAUTH authentication successful"
            )
        else:
            raise HTTPException(status_code=401, detail="Authentication failed")
            
    except Exception as e:
        logger.error(f"Authentication error: {str(e)}")
        await fibonrose_service.log_event(
            action="auth_error",
            metadata={"username": auth_request.username, "error": str(e)},
            user="system"
        )
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/entries", response_model=List[APIEntry])
async def get_api_entries(
    category: Optional[str] = None,
    search: Optional[str] = None,
    auth: Optional[str] = None,
    https: Optional[bool] = None,
    limit: int = 100
):
    """
    Fetch and filter API entries from public-apis.org
    """
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.get("https://api.publicapis.org/entries")
            response.raise_for_status()
            data = response.json()
            
            entries = data.get("entries", [])
            
            # Apply filters
            if category and category.lower() != "all":
                entries = [e for e in entries if e.get("Category") == category]
            
            if search:
                search_lower = search.lower()
                entries = [
                    e for e in entries 
                    if search_lower in e.get("API", "").lower() 
                    or search_lower in e.get("Description", "").lower()
                ]
            
            if auth:
                entries = [e for e in entries if e.get("Auth") == auth]
            
            if https is not None:
                entries = [e for e in entries if e.get("HTTPS") == https]
            
            # Limit results
            entries = entries[:limit]
            
            # Log the request
            await fibonrose_service.log_event(
                action="api_entries_fetched",
                metadata={
                    "count": len(entries),
                    "filters": {
                        "category": category,
                        "search": search,
                        "auth": auth,
                        "https": https
                    }
                },
                user="system"
            )
            
            return entries
            
    except httpx.HTTPError as e:
        logger.error(f"Error fetching API entries: {str(e)}")
        raise HTTPException(status_code=502, detail="Failed to fetch API entries")
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/categories")
async def get_categories():
    """
    Get list of all available API categories
    """
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.get("https://api.publicapis.org/entries")
            response.raise_for_status()
            data = response.json()
            
            entries = data.get("entries", [])
            categories = sorted(list(set(e.get("Category", "Unknown") for e in entries)))
            
            return {
                "categories": ["All"] + categories,
                "count": len(categories)
            }
            
    except Exception as e:
        logger.error(f"Error fetching categories: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/github", response_model=List[Dict[str, Any]])
async def get_github_api_endpoints(
    search: Optional[str] = None
):
    """
    Get comprehensive GitHub REST API endpoints
    
    Returns all GitHub API endpoints with detailed information including
    available endpoints for each category (repositories, issues, pulls, etc.)
    """
    try:
        # Get GitHub API endpoints from curated service
        endpoints = await curated_apis_service.get_github_endpoints(search=search)
        
        # Log the request
        await fibonrose_service.log_event(
            action="github_api_endpoints_fetched",
            metadata={
                "count": len(endpoints),
                "search": search
            },
            user="system"
        )
        
        return endpoints
        
    except Exception as e:
        logger.error(f"Error fetching GitHub API endpoints: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/enriched", response_model=List[Dict[str, Any]])
async def get_enriched_apis(
    search: Optional[str] = None,
    auth: Optional[str] = None,
    limit: int = 100
):
    """
    Get enriched collection of high-quality development APIs
    
    Returns curated collection of open-source and free development APIs including:
    - Version control (GitLab, Bitbucket)
    - Package registries (npm, PyPI, Maven)
    - CI/CD platforms (CircleCI, Travis CI)
    - Code quality tools (SonarQube, Codacy)
    - Documentation (Stack Exchange, DevDocs)
    - And many more...
    """
    try:
        # Get enriched APIs from curated service
        apis = await curated_apis_service.get_enriched_apis(
            search=search,
            auth=auth,
            limit=limit
        )
        
        # Log the request
        await fibonrose_service.log_event(
            action="enriched_apis_fetched",
            metadata={
                "count": len(apis),
                "filters": {
                    "search": search,
                    "auth": auth
                }
            },
            user="system"
        )
        
        return apis
        
    except Exception as e:
        logger.error(f"Error fetching enriched APIs: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/curated", response_model=List[Dict[str, Any]])
async def get_all_curated_apis(
    include_github: bool = True,
    include_enriched: bool = True,
    search: Optional[str] = None,
    limit: int = 200
):
    """
    Get all curated APIs (GitHub + enriched development APIs)
    
    Combines comprehensive GitHub REST API endpoints with a rich collection
    of open-source and free development APIs to provide a one-stop catalog
    for developers.
    """
    try:
        # Get all curated APIs
        apis = await curated_apis_service.get_all_curated_apis(
            include_github=include_github,
            include_enriched=include_enriched,
            search=search,
            limit=limit
        )
        
        # Log the request
        await fibonrose_service.log_event(
            action="curated_apis_fetched",
            metadata={
                "count": len(apis),
                "include_github": include_github,
                "include_enriched": include_enriched,
                "search": search
            },
            user="system"
        )
        
        return apis
        
    except Exception as e:
        logger.error(f"Error fetching curated APIs: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/generate", response_model=CodeGenerationResponse)
async def generate_code(
    request: CodeGenerationRequest,
    user: dict = Depends(verify_auth)
):
    """
    Generate full-stack code for selected API
    Requires DeafAUTH authentication
    """
    try:
        # Log code generation request
        await fibonrose_service.log_event(
            action="code_generation_started",
            metadata={
                "api_name": request.api_name,
                "category": request.category
            },
            user=user["username"]
        )
        
        # Generate code using the code generator service
        code = await code_generator_service.generate_fullstack_code(
            api_name=request.api_name,
            api_description=request.description,
            api_link=request.link,
            api_category=request.category,
            api_auth=request.auth,
            username=user["username"]
        )
        
        # Log successful generation
        await fibonrose_service.log_event(
            action="code_generation_completed",
            metadata={
                "api_name": request.api_name,
                "code_length": len(code)
            },
            user=user["username"]
        )
        
        return CodeGenerationResponse(
            success=True,
            code=code,
            api_name=request.api_name,
            generated_at=datetime.utcnow().isoformat(),
            mbtq_metadata={
                "deafauth": "✅ Validated",
                "fibonrose": "🌹 Logged",
                "pinksync": "⚡ Ready"
            }
        )
        
    except Exception as e:
        logger.error(f"Code generation error: {str(e)}")
        await fibonrose_service.log_event(
            action="code_generation_error",
            metadata={"error": str(e)},
            user=user["username"]
        )
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/deploy", response_model=DeploymentResponse)
async def deploy_api(
    request: DeploymentRequest,
    user: dict = Depends(verify_auth)
):
    """
    Deploy generated API to mbtq.dev via PinkSync
    Requires DeafAUTH authentication
    """
    try:
        # Log deployment initiation
        await fibonrose_service.log_event(
            action="deployment_started",
            metadata={
                "api_name": request.api_name,
                "target": "mbtq.dev"
            },
            user=user["username"]
        )
        
        # Execute deployment via PinkSync
        deployment_result = await pinksync_service.deploy(
            api_name=request.api_name,
            code=request.code,
            config=request.config,
            user=user["username"]
        )
        
        # Log deployment completion
        await fibonrose_service.log_event(
            action="deployment_completed",
            metadata={
                "api_name": request.api_name,
                "deployment_url": deployment_result["url"],
                "status": deployment_result["status"]
            },
            user=user["username"]
        )
        
        return DeploymentResponse(
            success=True,
            deployment_id=deployment_result["deployment_id"],
            url=deployment_result["url"],
            status=deployment_result["status"],
            logs=deployment_result["logs"],
            deployed_at=datetime.utcnow().isoformat()
        )
        
    except Exception as e:
        logger.error(f"Deployment error: {str(e)}")
        await fibonrose_service.log_event(
            action="deployment_error",
            metadata={
                "api_name": request.api_name,
                "error": str(e)
            },
            user=user["username"]
        )
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/deployments/{deployment_id}")
async def get_deployment_status(
    deployment_id: str,
    user: dict = Depends(verify_auth)
):
    """
    Get deployment status by ID
    """
    try:
        status = await pinksync_service.get_deployment_status(deployment_id)
        return status
    except Exception as e:
        logger.error(f"Error fetching deployment status: {str(e)}")
        raise HTTPException(status_code=404, detail="Deployment not found")


@app.get("/api/fibonrose/logs")
async def get_fibonrose_logs(
    user: dict = Depends(verify_auth),
    limit: int = 50
):
    """
    Get Fibonrose activity logs for authenticated user
    """
    try:
        logs = await fibonrose_service.get_user_logs(
            username=user["username"],
            limit=limit
        )
        return {
            "logs": logs,
            "count": len(logs),
            "user": user["username"]
        }
    except Exception as e:
        logger.error(f"Error fetching logs: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/fibonrose/reputation")
async def get_reputation(user: dict = Depends(verify_auth)):
    """
    Get user's Fibonrose reputation score
    """
    try:
        reputation = await fibonrose_service.get_reputation(user["username"])
        return reputation
    except Exception as e:
        logger.error(f"Error fetching reputation: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


# Error handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Custom HTTP exception handler"""
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.detail,
            "timestamp": datetime.utcnow().isoformat(),
            "path": str(request.url)
        }
    )


@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    """General exception handler"""
    logger.error(f"Unhandled exception: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error",
            "timestamp": datetime.utcnow().isoformat(),
            "path": str(request.url)
        }
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
