# MBTQ Auto-API - Architecture Documentation

## Overview

The MBTQ Auto-API is a comprehensive FastAPI-based system that provides visual-first API integration with automated deployment capabilities. It integrates three core MBTQ Universe services: DeafAUTH, Fibonrose, and PinkSync.

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     MBTQ Auto-API                            │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              FastAPI Application (main.py)            │  │
│  │                                                        │  │
│  │  • CORS Middleware                                    │  │
│  │  • Exception Handlers                                 │  │
│  │  • Route Definitions                                  │  │
│  │  • Dependency Injection                               │  │
│  └──────────────────────────────────────────────────────┘  │
│                           │                                  │
│                           ▼                                  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │                  Service Layer                        │  │
│  │                                                        │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  │  │
│  │  │  DeafAUTH   │  │ Fibonrose   │  │  PinkSync   │  │  │
│  │  │   Service   │  │   Service   │  │   Service   │  │  │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  │  │
│  │         │                 │                 │         │  │
│  │  ┌─────────────────────────────────────────────────┐ │  │
│  │  │         Code Generator Service                  │ │  │
│  │  └─────────────────────────────────────────────────┘ │  │
│  └──────────────────────────────────────────────────────┘  │
│                           │                                  │
│                           ▼                                  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │               Data Models (models.py)                 │  │
│  │  • Pydantic Models for Validation                    │  │
│  │  • Type Definitions                                   │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                   External Services                          │
│                                                              │
│  • public-apis.org (API Discovery)                          │
│  • Vercel (Deployment Target)                               │
│  • GitHub (Code Repository)                                 │
└─────────────────────────────────────────────────────────────┘
```

## Components

### 1. FastAPI Application (`main.py`)

**Purpose**: Core application server that handles HTTP requests and coordinates services.

**Key Features**:
- RESTful API endpoints
- CORS middleware for cross-origin requests
- Authentication middleware using DeafAUTH
- Automatic OpenAPI documentation
- Error handling and logging

**Endpoints**:
```
GET  /                          - API information
GET  /api/health                - Health check
POST /api/auth/login            - Authentication
GET  /api/entries               - API discovery
GET  /api/categories            - Category listing
POST /api/generate              - Code generation
POST /api/deploy                - Deployment
GET  /api/deployments/{id}      - Deployment status
GET  /api/fibonrose/logs        - Activity logs
GET  /api/fibonrose/reputation  - User reputation
```

### 2. Service Layer

#### DeafAUTH Service (`services/deafauth.py`)

**Purpose**: Handle user authentication and token management.

**Key Features**:
- Token generation using secure random tokens
- Token validation and expiration
- User session management
- In-memory storage (can be replaced with Redis/database)

**Methods**:
```python
authenticate(username, password) -> Dict
verify_token(token) -> Optional[Dict]
revoke_token(token) -> bool
get_user(username) -> Optional[Dict]
```

**Security**:
- Tokens are generated using `secrets.token_urlsafe(32)`
- 24-hour token expiration (configurable)
- Token validation on every protected endpoint

#### Fibonrose Service (`services/fibonrose.py`)

**Purpose**: Track user activity and manage reputation scores.

**Key Features**:
- Event logging with metadata
- Reputation point system
- Level progression (Novice → Grandmaster)
- Activity history tracking

**Reputation Impact**:
```
Authentication:              +5 points
API Entries Fetch:          +1 point
Code Generation Started:    +10 points
Code Generation Completed:  +20 points
Deployment Started:         +15 points
Deployment Completed:       +50 points
Errors:                     -5 to -25 points
```

**Levels**:
```
Novice:       0-49 points
Apprentice:   50-149 points
Adept:        150-299 points
Expert:       300-499 points
Master:       500-999 points
Grandmaster:  1000+ points
```

**Methods**:
```python
log_event(action, metadata, user) -> Dict
get_user_logs(username, limit) -> List[Dict]
get_reputation(username) -> Dict
get_leaderboard(limit) -> List[Dict]
```

#### PinkSync Service (`services/pinksync.py`)

**Purpose**: Handle API deployment to mbtq.dev (simulated).

**Key Features**:
- Simulated deployment process
- Detailed deployment logs
- Deployment status tracking
- URL generation

**Deployment Process**:
1. Create API endpoint files
2. Generate React component
3. Write configuration files
4. Push to GitHub (simulated)
5. Trigger build process
6. Deploy to production
7. Return deployment URL

**Methods**:
```python
deploy(api_name, code, config, user) -> Dict
get_deployment_status(deployment_id) -> Dict
get_user_deployments(username, limit) -> List[Dict]
delete_deployment(deployment_id) -> bool
```

#### Code Generator Service (`services/code_generator.py`)

**Purpose**: Generate full-stack code for API integrations.

**Generated Code Includes**:
- **FastAPI Backend**: Complete endpoint with authentication
- **React Frontend**: Component with data fetching
- **Vercel Configuration**: Deployment settings
- **Requirements**: Python dependencies
- **Documentation**: Integration instructions

**Methods**:
```python
generate_fullstack_code(
    api_name,
    api_description,
    api_link,
    api_category,
    api_auth,
    username
) -> str
```

### 3. Data Models (`models.py`)

**Purpose**: Define data structures and validation rules using Pydantic.

**Key Models**:
```python
APIEntry              - API entry from public-apis.org
APIFilter             - Filter parameters
AuthRequest           - Authentication request
AuthResponse          - Authentication response
CodeGenerationRequest - Code generation parameters
CodeGenerationResponse - Generated code response
DeploymentRequest     - Deployment parameters
DeploymentResponse    - Deployment result
FibonroseLog         - Activity log entry
FibonroseReputation  - User reputation data
```

**Benefits**:
- Automatic validation
- Type safety
- OpenAPI schema generation
- Clear data contracts

### 4. Configuration (`config.py`)

**Purpose**: Centralized configuration management using Pydantic Settings.

**Configuration Categories**:
- Application settings (name, version, debug)
- Server settings (host, port)
- CORS settings
- MBTQ service endpoints
- External API keys
- Token settings
- Rate limiting

**Environment Variables**: Loaded from `.env` file.

## Data Flow

### 1. Authentication Flow

```
Client → POST /api/auth/login
         ↓
    Validate credentials
         ↓
    Generate secure token
         ↓
    Store token in DeafAUTH
         ↓
    Log event in Fibonrose
         ↓
    Return token to client
```

### 2. Code Generation Flow

```
Client → POST /api/generate (with token)
         ↓
    Verify token with DeafAUTH
         ↓
    Log start event in Fibonrose
         ↓
    Generate full-stack code
         ↓
    Log completion in Fibonrose
         ↓
    Update user reputation
         ↓
    Return generated code
```

### 3. Deployment Flow

```
Client → POST /api/deploy (with token)
         ↓
    Verify token with DeafAUTH
         ↓
    Log start event in Fibonrose
         ↓
    Execute deployment via PinkSync
         ↓
    Generate deployment logs
         ↓
    Store deployment info
         ↓
    Log completion in Fibonrose
         ↓
    Update user reputation (+50 points)
         ↓
    Return deployment URL
```

## Storage Architecture

### Current Implementation (In-Memory)

**Suitable for**: Development, testing, small deployments

**Storage**:
- DeafAUTH: `Dict[token, user_data]`
- Fibonrose: `List[log_entry]`, `Dict[username, reputation]`
- PinkSync: `Dict[deployment_id, deployment_data]`

**Limitations**:
- Data lost on server restart
- No horizontal scaling
- Limited capacity

### Production Recommendations

**Database Layer**:
```python
# PostgreSQL for structured data
- Users and authentication
- Deployment records
- Reputation data

# Redis for caching
- Active tokens
- Rate limiting
- Session data

# MongoDB/Document DB for logs
- Activity logs
- Deployment logs
- Audit trails
```

## Security Architecture

### Authentication

**Token-Based Authentication**:
1. Client authenticates with username
2. Server generates secure token (32 bytes)
3. Token stored with 24-hour expiration
4. Client includes token in `X-MBTQ-Token` header
5. Server validates token on each request

**Token Format**: URL-safe random string (e.g., `nj6gsVl7hl_vWk6kxWT9C7bGlwek06htI4prmVql334`)

### Input Validation

All inputs are validated using Pydantic models:
- Type checking
- Length constraints
- Pattern matching
- Custom validators

### CORS Protection

CORS middleware configured to:
- Allow specific origins (currently `*` for development)
- Control allowed methods
- Manage credentials

### Dependency Security

All dependencies are:
- Regularly updated
- Scanned for vulnerabilities
- Using patched versions

## Scalability Considerations

### Horizontal Scaling

**Stateless Design**: Each request is independent, allowing multiple server instances.

**Required Changes for Production**:
1. Replace in-memory storage with Redis/database
2. Use distributed token storage
3. Implement session affinity if needed
4. Add load balancer

### Performance Optimization

**Current**:
- Async/await for I/O operations
- Connection pooling in httpx
- Efficient data structures

**Future Enhancements**:
- Response caching
- Database query optimization
- CDN for static content
- Background task queues

## Monitoring and Observability

### Logging

**Current Implementation**:
- Python logging module
- INFO level for normal operations
- ERROR level for failures

**Recommended for Production**:
- Structured logging (JSON)
- Centralized log aggregation (ELK, DataDog)
- Log correlation IDs
- Performance metrics

### Metrics

**Track**:
- Request rate
- Response times
- Error rates
- Active users
- Deployment success rate
- Reputation score distribution

### Health Checks

Implemented at `/api/health`:
- Service availability
- Database connectivity (when implemented)
- External service status

## Deployment Options

### 1. Vercel (Serverless)

**Configuration**: `vercel.json` provided

**Pros**:
- Zero-config deployment
- Auto-scaling
- Built-in CDN
- Free tier available

**Cons**:
- Stateless only
- Cold start latency
- Limited execution time

### 2. Docker (Containerized)

**Configuration**: `Dockerfile` provided

**Pros**:
- Consistent environments
- Easy local development
- Portable deployment
- Full control

**Cons**:
- Requires orchestration
- Infrastructure management

### 3. Traditional Server

**Run with**:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

**Pros**:
- Full control
- Stateful possible
- No cold starts

**Cons**:
- Manual scaling
- Infrastructure management

## Testing Strategy

### Unit Tests
Test individual components:
- Service methods
- Model validation
- Helper functions

### Integration Tests
Test component interactions:
- Endpoint flows
- Service coordination
- Error handling

### End-to-End Tests
Test complete workflows:
- Authentication → Generation → Deployment
- Reputation tracking
- Log aggregation

## Future Enhancements

### Planned Features
1. **Real MBTQ Service Integration**: Connect to actual DeafAUTH, Fibonrose, PinkSync services
2. **Database Integration**: Replace in-memory storage
3. **WebSocket Support**: Real-time deployment logs
4. **API Versioning**: Support multiple API versions
5. **Rate Limiting**: Implement per-user rate limits
6. **Caching**: Cache API discovery results
7. **Batch Operations**: Generate/deploy multiple APIs
8. **Team Features**: Multi-user deployments
9. **Analytics Dashboard**: Usage statistics
10. **Webhook Support**: Deployment notifications

### Technical Debt
1. Add comprehensive test suite
2. Implement proper error recovery
3. Add request/response logging
4. Implement circuit breakers for external services
5. Add API pagination
6. Implement background task processing

## Contributing

When contributing to this project:

1. **Follow the architecture**: Use service layer for business logic
2. **Add models**: Define Pydantic models for new data structures
3. **Document endpoints**: Update API_GUIDE.md
4. **Add tests**: Include tests for new features
5. **Security first**: Validate all inputs, sanitize outputs
6. **Log events**: Use Fibonrose for activity tracking

## References

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Uvicorn Documentation](https://www.uvicorn.org/)
- [Public APIs](https://github.com/public-apis/public-apis)

---

**Last Updated**: 2025-12-14  
**Version**: 1.0.0  
**Maintainer**: MBTQ Team
