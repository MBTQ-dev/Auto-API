# Contributing to MBTQ Auto-API

Thank you for your interest in contributing to MBTQ Auto-API! This document provides guidelines and instructions for contributing.

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [Getting Started](#getting-started)
3. [Development Setup](#development-setup)
4. [Making Changes](#making-changes)
5. [Testing](#testing)
6. [Documentation](#documentation)
7. [Pull Request Process](#pull-request-process)
8. [Style Guide](#style-guide)

## Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inclusive environment for all contributors, regardless of:
- Experience level
- Gender identity and expression
- Sexual orientation
- Disability
- Personal appearance
- Body size
- Race, ethnicity, or nationality
- Age
- Religion

### Expected Behavior

- Be respectful and considerate
- Use welcoming and inclusive language
- Accept constructive criticism gracefully
- Focus on what is best for the community
- Show empathy towards others

## Getting Started

### Prerequisites

- Python 3.11 or higher
- Git
- Basic understanding of FastAPI and async Python
- Familiarity with REST APIs

### Areas to Contribute

We welcome contributions in these areas:

1. **Bug Fixes**: Fix issues in existing code
2. **New Features**: Implement planned or new features
3. **Documentation**: Improve or add documentation
4. **Tests**: Add or improve test coverage
5. **Performance**: Optimize existing code
6. **Security**: Identify and fix security issues

## Development Setup

### 1. Fork and Clone

```bash
# Fork the repository on GitHub
# Then clone your fork
git clone https://github.com/YOUR_USERNAME/Auto-API.git
cd Auto-API
```

### 2. Set Up Virtual Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
# Install project dependencies
pip install -r requirements.txt

# Install development dependencies (if available)
pip install pytest pytest-asyncio pytest-cov black flake8
```

### 4. Set Up Configuration

```bash
# Copy example environment file
cp .env.example .env

# Edit .env with your settings (if needed)
```

### 5. Run the Server

```bash
# Start the development server
./start_server.sh

# Or manually
uvicorn main:app --reload
```

### 6. Verify Setup

```bash
# Test that the server is running
curl http://localhost:8000/api/health

# Run tests (if available)
python test_api.py
```

## Making Changes

### 1. Create a Branch

```bash
# Create a new branch for your changes
git checkout -b feature/your-feature-name

# Or for bug fixes
git checkout -b fix/bug-description
```

### 2. Write Code

Follow these guidelines:

#### Project Structure

```
Auto-API/
├── main.py              # FastAPI application (add endpoints here)
├── models.py            # Pydantic models (add data models here)
├── config.py            # Configuration (add settings here)
├── services/            # Service layer
│   ├── deafauth.py      # Authentication service
│   ├── fibonrose.py     # Logging/reputation service
│   ├── pinksync.py      # Deployment service
│   └── code_generator.py # Code generation service
└── tests/               # Test files (create this directory)
```

#### Adding a New Endpoint

1. **Define the model** in `models.py`:
```python
class NewFeatureRequest(BaseModel):
    field1: str
    field2: int
```

2. **Add the endpoint** in `main.py`:
```python
@app.post("/api/new-feature")
async def new_feature(request: NewFeatureRequest, user: dict = Depends(verify_auth)):
    # Your implementation
    await fibonrose_service.log_event("new_feature", {}, user["username"])
    return {"success": True}
```

3. **Update documentation**:
   - Add to API_GUIDE.md
   - Update README.md if needed

#### Adding a New Service

1. Create a new file in `services/`:
```python
# services/new_service.py

class NewService:
    def __init__(self):
        pass
    
    async def health_check(self) -> str:
        return "healthy"
    
    async def do_something(self, param: str) -> Dict:
        # Implementation
        pass
```

2. Import in `main.py`:
```python
from services.new_service import NewService

new_service = NewService()
```

### 3. Write Tests

Create tests for your changes:

```python
# tests/test_new_feature.py

import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_new_feature():
    async with AsyncClient(app=app, base_url="http://test") as client:
        # Authenticate first
        auth_response = await client.post(
            "/api/auth/login",
            json={"username": "testuser"}
        )
        token = auth_response.json()["token"]
        
        # Test your endpoint
        response = await client.post(
            "/api/new-feature",
            headers={"X-MBTQ-Token": token},
            json={"field1": "value", "field2": 123}
        )
        
        assert response.status_code == 200
        assert response.json()["success"] == True
```

### 4. Update Documentation

If your changes affect the API:

1. **Update API_GUIDE.md** with new endpoint documentation
2. **Update README.md** if adding major features
3. **Update CHANGELOG.md** under [Unreleased]
4. **Add docstrings** to new functions/classes

## Testing

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=. --cov-report=html

# Run specific test file
pytest tests/test_new_feature.py
```

### Writing Good Tests

- Test both success and failure cases
- Test edge cases
- Test authentication/authorization
- Test input validation
- Use meaningful test names
- Keep tests independent

### Manual Testing

```bash
# Start the server
uvicorn main:app --reload

# Test endpoints manually
curl -X POST http://localhost:8000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser"}'
```

## Documentation

### Code Documentation

Use docstrings for all public functions and classes:

```python
async def example_function(param: str) -> Dict:
    """
    Brief description of what this function does.
    
    Args:
        param: Description of the parameter
        
    Returns:
        Dict containing the result with keys:
        - success: Boolean indicating success
        - data: The actual data
        
    Raises:
        HTTPException: If validation fails
    """
    pass
```

### API Documentation

FastAPI generates automatic documentation, but also update:

1. **API_GUIDE.md**: Detailed endpoint documentation
2. **README.md**: High-level usage examples
3. **ARCHITECTURE.md**: For architectural changes

## Pull Request Process

### 1. Commit Your Changes

```bash
# Stage your changes
git add .

# Commit with a clear message
git commit -m "Add: Brief description of changes"

# Use conventional commit prefixes:
# - Add: New feature
# - Fix: Bug fix
# - Update: Update existing feature
# - Remove: Remove feature/code
# - Docs: Documentation only
# - Test: Add/update tests
# - Refactor: Code refactoring
```

### 2. Push to Your Fork

```bash
git push origin feature/your-feature-name
```

### 3. Create Pull Request

1. Go to the original repository on GitHub
2. Click "New Pull Request"
3. Select your fork and branch
4. Fill in the PR template:

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement

## Testing
- [ ] All tests pass
- [ ] New tests added
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guide
- [ ] Documentation updated
- [ ] No new warnings
- [ ] Security considerations addressed
```

### 4. Code Review

- Respond to reviewer comments
- Make requested changes
- Push updates to the same branch

### 5. After Merge

```bash
# Update your main branch
git checkout main
git pull upstream main

# Delete your feature branch
git branch -d feature/your-feature-name
```

## Style Guide

### Python Code Style

Follow PEP 8 with these specifics:

#### Formatting

```python
# Use 4 spaces for indentation (no tabs)
def example():
    pass

# Max line length: 100 characters
# Use black for formatting
black main.py

# Check with flake8
flake8 main.py
```

#### Naming Conventions

```python
# Classes: PascalCase
class MyService:
    pass

# Functions/Variables: snake_case
def my_function():
    my_variable = "value"

# Constants: UPPER_CASE
MAX_RETRIES = 3

# Private: _leading_underscore
def _private_helper():
    pass
```

#### Type Hints

Always use type hints:

```python
from typing import Optional, Dict, List

async def fetch_data(
    user_id: str,
    limit: int = 10
) -> Dict[str, Any]:
    pass
```

#### Async/Await

Use async/await consistently:

```python
# Good
async def fetch_data():
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()

# Avoid mixing sync/async without good reason
```

### Documentation Style

#### Markdown

- Use proper heading hierarchy
- Include code examples
- Add links where appropriate
- Use lists for clarity

#### Code Comments

```python
# Good: Explain WHY, not WHAT
# Calculate reputation based on recent activity
score = sum(log["impact"] for log in recent_logs)

# Avoid: Obvious comments
# Bad: Set score to sum of impacts
score = sum(log["impact"] for log in recent_logs)
```

### Commit Messages

Good commit messages:
```
Add: User authentication endpoint

- Implement token generation
- Add token validation
- Update documentation

Closes #123
```

Bad commit messages:
```
fix stuff
update
changes
```

## Recognition

Contributors will be:
- Listed in the repository contributors
- Acknowledged in release notes
- Credited in CHANGELOG.md

## Questions?

If you have questions:
1. Check existing documentation
2. Search existing issues
3. Ask in a new issue with the "question" label

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to MBTQ Auto-API! 🎯
