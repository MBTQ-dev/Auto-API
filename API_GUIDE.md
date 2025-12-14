# MBTQ Auto-API - Complete API Guide

## Table of Contents
1. [Introduction](#introduction)
2. [Authentication](#authentication)
3. [API Endpoints](#api-endpoints)
4. [Code Examples](#code-examples)
5. [Error Handling](#error-handling)
6. [Rate Limiting](#rate-limiting)

## Introduction

The MBTQ Auto-API provides a comprehensive FastAPI backend for discovering, generating, and deploying API integrations. It integrates with three core MBTQ services:

- **🔐 DeafAUTH**: Secure authentication and authorization
- **🌹 Fibonrose**: Activity logging and reputation system
- **⚡ PinkSync**: Automated deployment to mbtq.dev

## Authentication

### Login

**Endpoint**: `POST /api/auth/login`

**Request**:
```json
{
  "username": "your_username",
  "password": "optional_password"
}
```

**Response**:
```json
{
  "success": true,
  "token": "your_auth_token_here",
  "username": "your_username",
  "message": "DeafAUTH authentication successful"
}
```

**Example**:
```bash
curl -X POST http://localhost:8000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username": "developer"}'
```

### Using Authentication

Include the token in the `X-MBTQ-Token` header for all authenticated endpoints:

```bash
curl http://localhost:8000/api/generate \
  -H "X-MBTQ-Token: your_token_here"
```

## API Endpoints

### Health & Status

#### GET `/`
Root endpoint with API information.

**Response**:
```json
{
  "name": "MBTQ Auto-API",
  "version": "1.0.0",
  "status": "operational",
  "services": {
    "deafauth": "🔐 Active",
    "fibonrose": "🌹 Active",
    "pinksync": "⚡ Active"
  },
  "docs": "/api/docs"
}
```

#### GET `/api/health`
Health check for all services.

**Response**:
```json
{
  "status": "healthy",
  "timestamp": "2025-12-14T09:32:45.031Z",
  "services": {
    "deafauth": "healthy",
    "fibonrose": "healthy",
    "pinksync": "healthy"
  }
}
```

### API Discovery

#### GET `/api/entries`
Fetch and filter API entries from public-apis.org.

**Query Parameters**:
- `category` (string, optional): Filter by category
- `search` (string, optional): Search in API name or description
- `auth` (string, optional): Filter by auth type (apiKey, OAuth, X-Mashape-Key)
- `https` (boolean, optional): Filter HTTPS-only APIs
- `limit` (integer, default: 100): Maximum results to return

**Example**:
```bash
# Get all Development APIs
curl "http://localhost:8000/api/entries?category=Development&limit=10"

# Search for weather APIs
curl "http://localhost:8000/api/entries?search=weather"

# Get APIs requiring API key authentication
curl "http://localhost:8000/api/entries?auth=apiKey"
```

**Response**:
```json
[
  {
    "API": "GitHub",
    "Description": "Make requests to the GitHub API",
    "Auth": "apiKey",
    "HTTPS": true,
    "Cors": "yes",
    "Link": "https://api.github.com",
    "Category": "Development"
  }
]
```

#### GET `/api/categories`
Get list of all available categories.

**Response**:
```json
{
  "categories": ["All", "Animals", "Development", "Finance", ...],
  "count": 50
}
```

### Code Generation

#### POST `/api/generate`
Generate full-stack code for API integration.

**Authentication**: Required (X-MBTQ-Token header)

**Request Body**:
```json
{
  "api_name": "GitHub",
  "description": "GitHub REST API",
  "link": "https://api.github.com",
  "category": "Development",
  "auth": "apiKey",
  "https": true
}
```

**Response**:
```json
{
  "success": true,
  "code": "// Full-stack code here...",
  "api_name": "GitHub",
  "generated_at": "2025-12-14T09:32:45.031Z",
  "mbtq_metadata": {
    "deafauth": "✅ Validated",
    "fibonrose": "🌹 Logged",
    "pinksync": "⚡ Ready"
  }
}
```

**Generated Code Includes**:
- FastAPI backend endpoint
- React frontend component
- Vercel deployment configuration
- Requirements.txt
- Documentation

**Example**:
```bash
curl -X POST http://localhost:8000/api/generate \
  -H "Content-Type: application/json" \
  -H "X-MBTQ-Token: YOUR_TOKEN" \
  -d '{
    "api_name": "GitHub",
    "description": "GitHub REST API",
    "link": "https://api.github.com",
    "category": "Development",
    "auth": "apiKey",
    "https": true
  }'
```

### Deployment

#### POST `/api/deploy`
Deploy generated API to mbtq.dev via PinkSync.

**Authentication**: Required (X-MBTQ-Token header)

**Request Body**:
```json
{
  "api_name": "GitHub",
  "code": "// Generated code...",
  "config": {
    "name": "mbtq-github-api",
    "env_vars": {
      "API_KEY": "optional"
    }
  }
}
```

**Response**:
```json
{
  "success": true,
  "deployment_id": "uuid-here",
  "url": "https://mbtq.dev/api/github",
  "status": "deployed",
  "logs": [
    {
      "timestamp": "09:32:45",
      "message": "🚀 PinkSync: Initiating deployment...",
      "type": "info"
    },
    {
      "timestamp": "09:32:50",
      "message": "✅ Live at: https://mbtq.dev/api/github",
      "type": "success"
    }
  ],
  "deployed_at": "2025-12-14T09:32:45.031Z"
}
```

**Example**:
```bash
curl -X POST http://localhost:8000/api/deploy \
  -H "Content-Type: application/json" \
  -H "X-MBTQ-Token: YOUR_TOKEN" \
  -d '{
    "api_name": "GitHub",
    "code": "YOUR_GENERATED_CODE"
  }'
```

#### GET `/api/deployments/{deployment_id}`
Get deployment status by ID.

**Authentication**: Required (X-MBTQ-Token header)

**Response**:
```json
{
  "deployment_id": "uuid-here",
  "api_name": "GitHub",
  "url": "https://mbtq.dev/api/github",
  "status": "deployed",
  "created_at": "2025-12-14T09:32:45.031Z",
  "updated_at": "2025-12-14T09:32:50.031Z"
}
```

### Fibonrose - Activity Logs

#### GET `/api/fibonrose/logs`
Get activity logs for authenticated user.

**Authentication**: Required (X-MBTQ-Token header)

**Query Parameters**:
- `limit` (integer, default: 50): Maximum logs to return

**Response**:
```json
{
  "logs": [
    {
      "id": "uuid",
      "action": "code_generation_completed",
      "metadata": {
        "api_name": "GitHub",
        "code_length": 7030
      },
      "user": "developer",
      "timestamp": "2025-12-14T09:32:45.031Z",
      "reputation_impact": 20
    }
  ],
  "count": 10,
  "user": "developer"
}
```

**Example**:
```bash
curl http://localhost:8000/api/fibonrose/logs?limit=10 \
  -H "X-MBTQ-Token: YOUR_TOKEN"
```

### Fibonrose - Reputation

#### GET `/api/fibonrose/reputation`
Get user's reputation score and level.

**Authentication**: Required (X-MBTQ-Token header)

**Response**:
```json
{
  "username": "developer",
  "score": 150,
  "level": "Apprentice",
  "total_actions": 25,
  "last_activity": "2025-12-14T09:32:45.031Z",
  "recent_history": [
    {
      "action": "deployment_completed",
      "impact": 50,
      "timestamp": "2025-12-14T09:32:45.031Z"
    }
  ]
}
```

**Reputation Levels**:
- Novice: 0-49 points
- Apprentice: 50-149 points
- Adept: 150-299 points
- Expert: 300-499 points
- Master: 500-999 points
- Grandmaster: 1000+ points

**Reputation Points**:
| Action | Points |
|--------|--------|
| Authentication | +5 |
| API Entries Fetch | +1 |
| Code Generation Started | +10 |
| Code Generation Completed | +20 |
| Deployment Started | +15 |
| Deployment Completed | +50 |
| Authentication Error | -5 |
| Code Generation Error | -10 |
| Deployment Error | -25 |

## Code Examples

### Python

```python
import httpx
import asyncio

async def use_mbtq_api():
    base_url = "http://localhost:8000"
    
    async with httpx.AsyncClient() as client:
        # Authenticate
        response = await client.post(
            f"{base_url}/api/auth/login",
            json={"username": "developer"}
        )
        token = response.json()["token"]
        
        # Generate code
        response = await client.post(
            f"{base_url}/api/generate",
            headers={"X-MBTQ-Token": token},
            json={
                "api_name": "GitHub",
                "description": "GitHub REST API",
                "link": "https://api.github.com",
                "category": "Development",
                "auth": "apiKey",
                "https": True
            }
        )
        code = response.json()["code"]
        
        # Deploy
        response = await client.post(
            f"{base_url}/api/deploy",
            headers={"X-MBTQ-Token": token},
            json={"api_name": "GitHub", "code": code}
        )
        url = response.json()["url"]
        print(f"Deployed to: {url}")

asyncio.run(use_mbtq_api())
```

### JavaScript

```javascript
const axios = require('axios');

async function useMBTQAPI() {
  const baseURL = 'http://localhost:8000';
  
  // Authenticate
  const authResponse = await axios.post(`${baseURL}/api/auth/login`, {
    username: 'developer'
  });
  const token = authResponse.data.token;
  
  // Generate code
  const genResponse = await axios.post(
    `${baseURL}/api/generate`,
    {
      api_name: 'GitHub',
      description: 'GitHub REST API',
      link: 'https://api.github.com',
      category: 'Development',
      auth: 'apiKey',
      https: true
    },
    {
      headers: { 'X-MBTQ-Token': token }
    }
  );
  const code = genResponse.data.code;
  
  // Deploy
  const deployResponse = await axios.post(
    `${baseURL}/api/deploy`,
    { api_name: 'GitHub', code },
    {
      headers: { 'X-MBTQ-Token': token }
    }
  );
  console.log(`Deployed to: ${deployResponse.data.url}`);
}

useMBTQAPI();
```

### cURL

```bash
# 1. Authenticate
TOKEN=$(curl -X POST http://localhost:8000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username": "developer"}' | jq -r '.token')

# 2. Generate code
CODE=$(curl -X POST http://localhost:8000/api/generate \
  -H "Content-Type: application/json" \
  -H "X-MBTQ-Token: $TOKEN" \
  -d '{
    "api_name": "GitHub",
    "description": "GitHub REST API",
    "link": "https://api.github.com",
    "category": "Development",
    "auth": "apiKey",
    "https": true
  }' | jq -r '.code')

# 3. Deploy
curl -X POST http://localhost:8000/api/deploy \
  -H "Content-Type: application/json" \
  -H "X-MBTQ-Token: $TOKEN" \
  -d "{\"api_name\": \"GitHub\", \"code\": $(echo $CODE | jq -R .)}"
```

## Error Handling

All errors follow a consistent format:

```json
{
  "error": "Error message here",
  "timestamp": "2025-12-14T09:32:45.031Z",
  "path": "/api/endpoint"
}
```

### Common HTTP Status Codes

- `200 OK`: Request successful
- `401 Unauthorized`: Missing or invalid DeafAUTH token
- `404 Not Found`: Resource not found
- `422 Unprocessable Entity`: Invalid request body
- `500 Internal Server Error`: Server error
- `502 Bad Gateway`: External service unavailable

### Example Error Response

```json
{
  "error": "DeafAUTH token required",
  "timestamp": "2025-12-14T09:32:45.031Z",
  "path": "/api/generate"
}
```

## Rate Limiting

The API implements rate limiting to ensure fair usage:

- **Default**: 60 requests per minute per user
- Headers included in responses:
  - `X-RateLimit-Limit`: Maximum requests per window
  - `X-RateLimit-Remaining`: Remaining requests
  - `X-RateLimit-Reset`: Time when limit resets

## Interactive Documentation

FastAPI provides automatic interactive documentation:

- **Swagger UI**: http://localhost:8000/api/docs
- **ReDoc**: http://localhost:8000/api/redoc

These interfaces allow you to:
- Browse all endpoints
- View request/response schemas
- Test endpoints directly in the browser
- Download OpenAPI specification

## Support

For issues, questions, or contributions:
- GitHub: https://github.com/MBTQ-dev/Auto-API
- Documentation: See README.md

---

**Made with ❤️ by the MBTQ Team**
