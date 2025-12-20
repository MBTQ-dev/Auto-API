# MBTQ Auto-API - Usage Examples

This guide demonstrates how to use the new GitHub REST API and enriched development APIs endpoints.

## Table of Contents
1. [GitHub REST API Endpoints](#github-rest-api-endpoints)
2. [Enriched Development APIs](#enriched-development-apis)
3. [Combined Curated APIs](#combined-curated-apis)
4. [Integration Examples](#integration-examples)

## GitHub REST API Endpoints

### Get All GitHub API Endpoints

```bash
curl http://localhost:8000/api/github
```

**Response:** Returns 15 comprehensive GitHub API endpoint categories including:
- Repositories, Issues, Pull Requests
- Commits, Branches, Users
- Organizations, Gists, Actions
- Releases, Search, Webhooks
- Contents, Notifications, Projects

### Search GitHub APIs

```bash
# Search for Issues API
curl "http://localhost:8000/api/github?search=issues"

# Search for Pull Requests
curl "http://localhost:8000/api/github?search=pull"

# Search for Webhooks
curl "http://localhost:8000/api/github?search=webhook"
```

### Example Response

```json
{
  "API": "GitHub - Issues",
  "Description": "Manage issues, comments, labels, and milestones",
  "Auth": "apiKey",
  "HTTPS": true,
  "Cors": "yes",
  "Link": "https://api.github.com/repos/{owner}/{repo}/issues",
  "Category": "Development",
  "SubCategory": "GitHub",
  "Endpoints": [
    "GET /repos/{owner}/{repo}/issues",
    "GET /repos/{owner}/{repo}/issues/{issue_number}",
    "POST /repos/{owner}/{repo}/issues",
    "PATCH /repos/{owner}/{repo}/issues/{issue_number}",
    "GET /repos/{owner}/{repo}/issues/{issue_number}/comments",
    "POST /repos/{owner}/{repo}/issues/{issue_number}/comments"
  ]
}
```

## Enriched Development APIs

### Get All Enriched APIs

```bash
curl http://localhost:8000/api/enriched
```

**Response:** Returns 37+ high-quality development APIs including:
- Version Control: GitLab, Bitbucket
- Package Registries: npm, PyPI, Maven, crates.io
- CI/CD: CircleCI, Travis CI, Vercel, Netlify
- Code Quality: SonarQube, Codacy
- And many more...

### Search Enriched APIs

```bash
# Search for Docker APIs
curl "http://localhost:8000/api/enriched?search=docker"

# Search for npm
curl "http://localhost:8000/api/enriched?search=npm"

# Search for CI/CD tools
curl "http://localhost:8000/api/enriched?search=ci"
```

### Filter by Authentication Type

```bash
# Get APIs that require API key authentication
curl "http://localhost:8000/api/enriched?auth=apiKey&limit=20"

# Get APIs with OAuth authentication
curl "http://localhost:8000/api/enriched?auth=OAuth&limit=10"

# Get APIs without authentication
curl "http://localhost:8000/api/enriched?auth="
```

### Example Response

```json
{
  "API": "Docker Hub API",
  "Description": "Access Docker container images and repositories",
  "Auth": "apiKey",
  "HTTPS": true,
  "Cors": "yes",
  "Link": "https://hub.docker.com/v2",
  "Category": "Development"
}
```

## Combined Curated APIs

### Get All Curated APIs

```bash
# Get both GitHub and enriched APIs (default)
curl http://localhost:8000/api/curated
```

### Filter Curated APIs

```bash
# Get only GitHub APIs
curl "http://localhost:8000/api/curated?include_enriched=false"

# Get only enriched APIs
curl "http://localhost:8000/api/curated?include_github=false"

# Search across all curated APIs
curl "http://localhost:8000/api/curated?search=api&limit=50"

# Limit results
curl "http://localhost:8000/api/curated?limit=10"
```

## Integration Examples

### Python Example

```python
import httpx
import asyncio

async def explore_apis():
    base_url = "http://localhost:8000"
    
    async with httpx.AsyncClient() as client:
        # Get GitHub APIs
        print("=== GitHub REST API Endpoints ===")
        response = await client.get(f"{base_url}/api/github")
        github_apis = response.json()
        print(f"Found {len(github_apis)} GitHub API categories")
        
        # Search for specific GitHub API
        response = await client.get(f"{base_url}/api/github?search=issues")
        issues_api = response.json()
        print(f"\nGitHub Issues API:")
        print(f"  - Link: {issues_api[0]['Link']}")
        print(f"  - Endpoints: {len(issues_api[0]['Endpoints'])} available")
        
        # Get enriched development APIs
        print("\n=== Enriched Development APIs ===")
        response = await client.get(f"{base_url}/api/enriched?limit=10")
        enriched_apis = response.json()
        print(f"Found {len(enriched_apis)} enriched APIs")
        
        for api in enriched_apis[:3]:
            print(f"\n{api['API']}")
            print(f"  - {api['Description']}")
            print(f"  - Link: {api['Link']}")
        
        # Search for Docker
        response = await client.get(f"{base_url}/api/enriched?search=docker")
        docker_apis = response.json()
        print(f"\n=== Docker APIs ===")
        for api in docker_apis:
            print(f"{api['API']}: {api['Link']}")
        
        # Get all curated APIs
        response = await client.get(f"{base_url}/api/curated?limit=5")
        curated_apis = response.json()
        print(f"\n=== Sample Curated APIs ===")
        for api in curated_apis:
            print(f"- {api['API']}")

asyncio.run(explore_apis())
```

### JavaScript Example

```javascript
const axios = require('axios');

async function exploreAPIs() {
  const baseURL = 'http://localhost:8000';
  
  try {
    // Get GitHub APIs
    console.log('=== GitHub REST API Endpoints ===');
    const githubResponse = await axios.get(`${baseURL}/api/github`);
    console.log(`Found ${githubResponse.data.length} GitHub API categories`);
    
    // Search for webhooks
    const webhooksResponse = await axios.get(`${baseURL}/api/github?search=webhook`);
    const webhook = webhooksResponse.data[0];
    console.log(`\nGitHub Webhooks API:`);
    console.log(`  - Link: ${webhook.Link}`);
    console.log(`  - Available endpoints: ${webhook.Endpoints.length}`);
    
    // Get enriched APIs
    console.log('\n=== Enriched Development APIs ===');
    const enrichedResponse = await axios.get(`${baseURL}/api/enriched?limit=10`);
    console.log(`Found ${enrichedResponse.data.length} enriched APIs`);
    
    enrichedResponse.data.slice(0, 3).forEach(api => {
      console.log(`\n${api.API}`);
      console.log(`  - ${api.Description}`);
      console.log(`  - Link: ${api.Link}`);
    });
    
    // Search for npm
    const npmResponse = await axios.get(`${baseURL}/api/enriched?search=npm`);
    console.log('\n=== npm Registry API ===');
    npmResponse.data.forEach(api => {
      console.log(`${api.API}: ${api.Link}`);
    });
    
    // Get APIs without authentication
    const noAuthResponse = await axios.get(`${baseURL}/api/enriched?auth=`);
    console.log(`\n=== APIs Without Authentication ===`);
    console.log(`Found ${noAuthResponse.data.length} APIs that don't require auth`);
    
  } catch (error) {
    console.error('Error:', error.message);
  }
}

exploreAPIs();
```

### cURL Examples

```bash
#!/bin/bash

echo "=== Testing MBTQ Auto-API - Curated APIs ==="

# Test 1: Get all GitHub API endpoints
echo -e "\n1. GitHub API Endpoints:"
curl -s http://localhost:8000/api/github | python -m json.tool | head -30

# Test 2: Search for specific GitHub API
echo -e "\n2. Search GitHub APIs for 'issues':"
curl -s "http://localhost:8000/api/github?search=issues" | python -m json.tool

# Test 3: Get enriched development APIs
echo -e "\n3. First 5 Enriched APIs:"
curl -s "http://localhost:8000/api/enriched?limit=5" | python -m json.tool

# Test 4: Search for Docker
echo -e "\n4. Search for Docker:"
curl -s "http://localhost:8000/api/enriched?search=docker" | python -m json.tool

# Test 5: Get APIs by authentication type
echo -e "\n5. APIs with API Key authentication (limit 5):"
curl -s "http://localhost:8000/api/enriched?auth=apiKey&limit=5" | python -m json.tool

# Test 6: Get all curated APIs
echo -e "\n6. Combined curated APIs (limit 10):"
curl -s "http://localhost:8000/api/curated?limit=10" | python -m json.tool

# Test 7: Count all APIs
echo -e "\n7. API Counts:"
echo -n "GitHub APIs: "
curl -s http://localhost:8000/api/github | python -c "import sys,json; print(len(json.load(sys.stdin)))"
echo -n "Enriched APIs: "
curl -s http://localhost:8000/api/enriched | python -c "import sys,json; print(len(json.load(sys.stdin)))"
```

## Use Cases

### 1. Building a Developer Portal

Use the curated APIs to build a comprehensive developer portal:

```python
# Fetch all APIs and categorize them
all_apis = await client.get(f"{base_url}/api/curated")

# Group by category
categorized = {}
for api in all_apis.json():
    category = api.get('Category', 'Other')
    if category not in categorized:
        categorized[category] = []
    categorized[category].append(api)

# Display in your portal
for category, apis in categorized.items():
    print(f"\n### {category} ({len(apis)} APIs)")
    for api in apis:
        print(f"  - {api['API']}: {api['Description']}")
```

### 2. API Discovery Tool

Create a tool to help developers find the right API:

```python
async def find_api(keyword):
    # Search across all curated APIs
    response = await client.get(
        f"{base_url}/api/curated?search={keyword}"
    )
    results = response.json()
    
    print(f"Found {len(results)} APIs matching '{keyword}':")
    for api in results:
        print(f"\n{api['API']}")
        print(f"  Description: {api['Description']}")
        print(f"  Link: {api['Link']}")
        print(f"  Auth: {api.get('Auth', 'None')}")
        if 'Endpoints' in api:
            print(f"  Endpoints: {', '.join(api['Endpoints'][:3])}...")
```

### 3. Documentation Generator

Generate API documentation automatically:

```python
async def generate_docs():
    # Get all GitHub APIs
    github_apis = await client.get(f"{base_url}/api/github")
    
    with open('github_api_docs.md', 'w') as f:
        f.write("# GitHub REST API Reference\n\n")
        
        for api in github_apis.json():
            f.write(f"## {api['API']}\n\n")
            f.write(f"{api['Description']}\n\n")
            f.write(f"**Base URL:** {api['Link']}\n\n")
            f.write(f"**Authentication:** {api['Auth']}\n\n")
            f.write("### Available Endpoints\n\n")
            
            for endpoint in api.get('Endpoints', []):
                f.write(f"- `{endpoint}`\n")
            
            f.write("\n---\n\n")
    
    print("Documentation generated: github_api_docs.md")
```

## Health Check

Always verify the service is healthy before making requests:

```bash
curl http://localhost:8000/api/health
```

Expected response:
```json
{
  "status": "healthy",
  "timestamp": "2025-12-20T04:11:01.718588",
  "services": {
    "deafauth": "healthy",
    "fibonrose": "healthy",
    "pinksync": "healthy",
    "curated_apis": "healthy"
  }
}
```

## Interactive Documentation

Access the interactive Swagger UI documentation at:
- **Swagger UI**: http://localhost:8000/api/docs
- **ReDoc**: http://localhost:8000/api/redoc

This allows you to:
- Browse all endpoints
- View request/response schemas
- Test endpoints directly in the browser
- Download OpenAPI specification

## Summary

The MBTQ Auto-API now provides:
- **15 GitHub REST API endpoint categories** covering all major GitHub functionality
- **37+ curated development APIs** for package registries, CI/CD, code quality, and more
- **Flexible search and filtering** across all APIs
- **Comprehensive documentation** for easy integration

All APIs are production-ready and can be integrated with the existing MBTQ services (DeafAUTH, Fibonrose, PinkSync) for authentication, logging, and deployment.

---

**Made with ❤️ by the MBTQ Team**
