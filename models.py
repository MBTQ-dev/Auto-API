"""
Data models for MBTQ Auto-API
"""

from pydantic import BaseModel, Field, field_validator
from typing import Optional, List, Dict, Any
from datetime import datetime


class APIEntry(BaseModel):
    """Model for API entry from public-apis.org"""
    API: str
    Description: str
    Auth: Optional[str] = None
    HTTPS: bool
    Cors: str
    Link: str
    Category: str


class APIFilter(BaseModel):
    """Model for filtering API entries"""
    category: Optional[str] = None
    search: Optional[str] = None
    auth: Optional[str] = None
    https: Optional[bool] = None
    limit: int = Field(default=100, ge=1, le=500)


class AuthRequest(BaseModel):
    """Model for authentication request"""
    username: str = Field(..., min_length=1, max_length=100)
    password: Optional[str] = None
    
    @field_validator('username')
    @classmethod
    def username_alphanumeric(cls, v):
        if not v.replace('_', '').replace('-', '').isalnum():
            raise ValueError('Username must be alphanumeric (with _ or - allowed)')
        return v


class AuthResponse(BaseModel):
    """Model for authentication response"""
    success: bool
    token: str
    username: str
    message: str
    expires_at: Optional[str] = None


class CodeGenerationRequest(BaseModel):
    """Model for code generation request"""
    api_name: str
    description: str
    link: str
    category: str
    auth: Optional[str] = None
    https: bool = True


class CodeGenerationResponse(BaseModel):
    """Model for code generation response"""
    success: bool
    code: str
    api_name: str
    generated_at: str
    mbtq_metadata: Dict[str, str]


class DeploymentConfig(BaseModel):
    """Model for deployment configuration"""
    name: Optional[str] = None
    env_vars: Optional[Dict[str, str]] = None
    build_command: Optional[str] = None
    output_directory: Optional[str] = None


class DeploymentRequest(BaseModel):
    """Model for deployment request"""
    api_name: str
    code: str
    config: Optional[DeploymentConfig] = None


class DeploymentLog(BaseModel):
    """Model for deployment log entry"""
    timestamp: str
    message: str
    type: str = Field(default="info")  # info, success, error, warning


class DeploymentResponse(BaseModel):
    """Model for deployment response"""
    success: bool
    deployment_id: str
    url: str
    status: str
    logs: List[DeploymentLog]
    deployed_at: str


class FibonroseLog(BaseModel):
    """Model for Fibonrose activity log"""
    id: Optional[str] = None
    action: str
    metadata: Dict[str, Any]
    user: str
    timestamp: str
    reputation_impact: int = 0


class FibonroseReputation(BaseModel):
    """Model for user reputation"""
    username: str
    score: int
    level: str
    total_actions: int
    last_activity: str


class HealthCheck(BaseModel):
    """Model for health check response"""
    status: str
    timestamp: str
    version: Optional[str] = None
