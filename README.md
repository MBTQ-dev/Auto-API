# 🎯 MBTQ Auto-API

**Visual-first API integration with auto-deployment to mbtq.dev**

[![FastAPI](https://img.shields.io/badge/FastAPI-0.109.1-009688.svg)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB.svg)](https://www.python.org)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## 🌟 Features

- **🔐 DeafAUTH Integration** - Secure authentication system
- **🌹 Fibonrose Tracking** - Reputation and activity logging
- **⚡ PinkSync Deployment** - Auto-deploy APIs to mbtq.dev
- **🎨 Full-Stack Code Generation** - Generate complete API integrations
- **📡 Public API Discovery** - Browse and integrate 1000+ public APIs
- **🐙 Complete GitHub REST API** - Full access to all GitHub API endpoints
- **🎯 Curated Developer APIs** - 40+ high-quality open-source development APIs
- **🚀 FastAPI Backend** - High-performance async API server
- **📊 Real-time Activity Logs** - Track all API interactions
- **🏆 Reputation System** - Gamified user engagement

## 🏗️ Architecture

The MBTQ Auto-API system consists of:

1. **FastAPI Backend** (`main.py`) - Core API server
2. **React Frontend** (`app.tsx`) - Visual interface
3. **MBTQ Services**:
   - **DeafAUTH** - Authentication & authorization
   - **Fibonrose** - Activity logging & reputation
   - **PinkSync** - Deployment automation
4. **Code Generator** - Full-stack code generation

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- pip or poetry

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/MBTQ-dev/Auto-API.git
   cd Auto-API
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment** (optional)
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

4. **Run the server**
   ```bash
   uvicorn main:app --reload
   ```

5. **Access the API**
   - API Server: http://localhost:8000
   - Interactive Docs: http://localhost:8000/api/docs
   - ReDoc: http://localhost:8000/api/redoc

## 📚 API Documentation

### Authentication Endpoints

#### POST `/api/auth/login`
Authenticate with DeafAUTH and receive a token.

**Request Body:**
```json
{
  "username": "your_username",
  "password": "your_password"
}
```

**Response:**
```json
{
  "success": true,
  "token": "your_auth_token",
  "username": "your_username",
  "message": "DeafAUTH authentication successful"
}
```

### API Discovery Endpoints

#### GET `/api/entries`
Fetch and filter API entries from public-apis.org.

**Query Parameters:**
- `category` (optional): Filter by category
- `search` (optional): Search term
- `auth` (optional): Filter by auth type
- `https` (optional): Filter HTTPS only
- `limit` (default: 100): Maximum results

**Example:**
```bash
curl http://localhost:8000/api/entries?category=Development&limit=10
```

#### GET `/api/categories`
Get list of all available API categories.

#### GET `/api/github`
Get comprehensive GitHub REST API endpoints.

**Query Parameters:**
- `search` (optional): Search term to filter GitHub endpoints

**Example:**
```bash
curl http://localhost:8000/api/github
curl http://localhost:8000/api/github?search=issues
```

**Returns:** Complete collection of GitHub REST API endpoints including:
- Repositories, Issues, Pull Requests
- Commits, Branches, Users
- Organizations, Gists, Actions
- Releases, Search, Webhooks
- Contents, Notifications, Projects

#### GET `/api/enriched`
Get curated collection of high-quality open-source/free development APIs.

**Query Parameters:**
- `search` (optional): Search term
- `auth` (optional): Filter by auth type
- `limit` (default: 100): Maximum results

**Example:**
```bash
curl http://localhost:8000/api/enriched
curl http://localhost:8000/api/enriched?search=docker
```

**Returns:** Enriched API collection including:
- Version Control: GitLab, Bitbucket
- Package Registries: npm, PyPI, Maven, crates.io
- CI/CD: CircleCI, Travis CI, Vercel, Netlify
- Code Quality: SonarQube, Codacy
- Documentation: Stack Exchange, DevDocs
- And 30+ more development APIs!

#### GET `/api/curated`
Get all curated APIs (GitHub + enriched APIs combined).

**Query Parameters:**
- `include_github` (default: true): Include GitHub endpoints
- `include_enriched` (default: true): Include enriched APIs
- `search` (optional): Search term
- `limit` (default: 200): Maximum results

**Example:**
```bash
curl http://localhost:8000/api/curated
curl "http://localhost:8000/api/curated?search=api&limit=50"
```


### Code Generation Endpoints

#### POST `/api/generate`
Generate full-stack code for selected API.

**Headers:**
- `X-MBTQ-Token`: Your DeafAUTH token (required)

**Request Body:**
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

**Response:**
```json
{
  "success": true,
  "code": "// Generated code...",
  "api_name": "GitHub",
  "generated_at": "2025-12-14T09:32:45.031Z",
  "mbtq_metadata": {
    "deafauth": "✅ Validated",
    "fibonrose": "🌹 Logged",
    "pinksync": "⚡ Ready"
  }
}
```

### Deployment Endpoints

#### POST `/api/deploy`
Deploy generated API to mbtq.dev.

**Headers:**
- `X-MBTQ-Token`: Your DeafAUTH token (required)

**Request Body:**
```json
{
  "api_name": "GitHub",
  "code": "// Your generated code...",
  "config": {
    "name": "mbtq-github-api",
    "env_vars": {}
  }
}
```

**Response:**
```json
{
  "success": true,
  "deployment_id": "uuid",
  "url": "https://mbtq.dev/api/github",
  "status": "deployed",
  "logs": [...],
  "deployed_at": "2025-12-14T09:32:45.031Z"
}
```

#### GET `/api/deployments/{deployment_id}`
Get deployment status by ID.

### Fibonrose Endpoints

#### GET `/api/fibonrose/logs`
Get activity logs for authenticated user.

**Headers:**
- `X-MBTQ-Token`: Your DeafAUTH token (required)

**Query Parameters:**
- `limit` (default: 50): Maximum number of logs

#### GET `/api/fibonrose/reputation`
Get user's reputation score and level.

**Headers:**
- `X-MBTQ-Token`: Your DeafAUTH token (required)

**Response:**
```json
{
  "username": "your_username",
  "score": 150,
  "level": "Apprentice",
  "total_actions": 25,
  "last_activity": "2025-12-14T09:32:45.031Z"
}
```

### Health Check

#### GET `/api/health`
Check service health status.

**Response:**
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

## 🎮 Usage Examples

### 1. Authenticate
```bash
curl -X POST http://localhost:8000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username": "developer", "password": "optional"}'
```

### 2. Browse APIs
```bash
curl http://localhost:8000/api/entries?category=Development
```

### 3. Generate Code
```bash
curl -X POST http://localhost:8000/api/generate \
  -H "Content-Type: application/json" \
  -H "X-MBTQ-Token: your_token" \
  -d '{
    "api_name": "GitHub",
    "description": "GitHub REST API",
    "link": "https://api.github.com",
    "category": "Development",
    "auth": "apiKey"
  }'
```

### 4. Deploy API
```bash
curl -X POST http://localhost:8000/api/deploy \
  -H "Content-Type: application/json" \
  -H "X-MBTQ-Token: your_token" \
  -d '{
    "api_name": "GitHub",
    "code": "your_generated_code"
  }'
```

## 🏆 Reputation System

Fibonrose tracks user activity and awards reputation points:

| Action | Points |
|--------|--------|
| Authentication | +5 |
| API Entries Fetch | +1 |
| Code Generation Started | +10 |
| Code Generation Completed | +20 |
| Deployment Started | +15 |
| Deployment Completed | +50 |
| Error Actions | -5 to -25 |

### Reputation Levels

- **Novice**: 0-49 points
- **Apprentice**: 50-149 points
- **Adept**: 150-299 points
- **Expert**: 300-499 points
- **Master**: 500-999 points
- **Grandmaster**: 1000+ points

## 🔧 Configuration

Configuration is managed through environment variables. See `.env.example` for all available options.

Key settings:
- `APP_NAME`: Application name
- `DEBUG`: Enable debug mode
- `HOST`: Server host
- `PORT`: Server port
- `TOKEN_EXPIRY_HOURS`: Token validity period
- `RATE_LIMIT_PER_MINUTE`: API rate limiting

## 🐳 Docker Deployment

Build and run with Docker:

```bash
docker build -t mbtq-auto-api .
docker run -p 8000:8000 mbtq-auto-api
```

## ☁️ Vercel Deployment

Deploy to Vercel:

```bash
vercel deploy
```

The `vercel.json` configuration is included.

## 🧪 Development

### Project Structure

```
Auto-API/
├── main.py              # FastAPI application
├── models.py            # Pydantic models
├── config.py            # Configuration
├── requirements.txt     # Python dependencies
├── services/
│   ├── __init__.py
│   ├── deafauth.py      # Authentication service
│   ├── fibonrose.py     # Logging & reputation
│   ├── pinksync.py      # Deployment service
│   └── code_generator.py # Code generation
├── app.tsx              # React frontend
├── Dockerfile           # Docker configuration
├── vercel.json          # Vercel deployment
└── README.md
```

### Running in Development Mode

```bash
uvicorn main:app --reload --log-level debug
```

## 🔒 Security

- All API endpoints requiring authentication use DeafAUTH tokens
- Tokens are validated on each request
- CORS is configured (customize for production)
- Input validation using Pydantic
- Dependencies are vulnerability-free

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📝 License

MIT License - see LICENSE file for details.

## 🌐 MBTQ Universe

Part of the MBTQ Universe ecosystem:
- **DeafAUTH**: Authentication system
- **Fibonrose**: Reputation & logging
- **PinkSync**: Deployment automation
- **360 Magicians**: AI assistance
- **Auto-API**: This project!

## 📧 Support

For issues and questions:
- GitHub Issues: https://github.com/MBTQ-dev/Auto-API/issues
- Documentation: https://github.com/MBTQ-dev/Auto-API

## 🎉 Acknowledgments

- Built with [FastAPI](https://fastapi.tiangolo.com/)
- API data from [Public APIs](https://github.com/public-apis/public-apis)
- Powered by the MBTQ Universe

---

**Made with ❤️ by the MBTQ Team**

🔐 DeafAUTH Protected | 🌹 Fibonrose Tracked | ⚡ PinkSync Deployed
