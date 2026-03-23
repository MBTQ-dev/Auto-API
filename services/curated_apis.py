"""
Curated APIs Service - Provides enriched API collections
Includes comprehensive GitHub REST API and other high-quality development APIs
"""

import logging

logger = logging.getLogger(__name__)


class CuratedAPIsService:
    """
    Service for providing curated, enriched API collections including:
    - Full GitHub REST API endpoints
    - High-quality open-source development APIs
    - Free APIs that enrich the Auto-API system
    """
    
    def __init__(self):
        self._github_api_endpoints = self._load_github_endpoints()
        self._enriched_apis = self._load_enriched_apis()
    
    def _load_github_endpoints(self) -> list:
        """
        Load comprehensive GitHub REST API endpoints
        Based on GitHub API v3 (REST) documentation
        """
        return [
            {
                "API": "GitHub - Repositories",
                "Description": "List, create, update, and delete repositories",
                "Auth": "apiKey",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://api.github.com/repos",
                "Category": "Development",
                "SubCategory": "GitHub",
                "Endpoints": [
                    "GET /repos/{owner}/{repo}",
                    "GET /user/repos",
                    "GET /orgs/{org}/repos",
                    "POST /user/repos",
                    "PATCH /repos/{owner}/{repo}",
                    "DELETE /repos/{owner}/{repo}"
                ]
            },
            {
                "API": "GitHub - Issues",
                "Description": "Manage issues, comments, labels, and milestones",
                "Auth": "apiKey",
                "HTTPS": True,
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
            },
            {
                "API": "GitHub - Pull Requests",
                "Description": "Create and manage pull requests",
                "Auth": "apiKey",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://api.github.com/repos/{owner}/{repo}/pulls",
                "Category": "Development",
                "SubCategory": "GitHub",
                "Endpoints": [
                    "GET /repos/{owner}/{repo}/pulls",
                    "GET /repos/{owner}/{repo}/pulls/{pull_number}",
                    "POST /repos/{owner}/{repo}/pulls",
                    "PATCH /repos/{owner}/{repo}/pulls/{pull_number}",
                    "GET /repos/{owner}/{repo}/pulls/{pull_number}/files",
                    "POST /repos/{owner}/{repo}/pulls/{pull_number}/reviews"
                ]
            },
            {
                "API": "GitHub - Commits",
                "Description": "Access commit history and details",
                "Auth": "apiKey",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://api.github.com/repos/{owner}/{repo}/commits",
                "Category": "Development",
                "SubCategory": "GitHub",
                "Endpoints": [
                    "GET /repos/{owner}/{repo}/commits",
                    "GET /repos/{owner}/{repo}/commits/{ref}",
                    "GET /repos/{owner}/{repo}/commits/{sha}",
                    "POST /repos/{owner}/{repo}/git/commits"
                ]
            },
            {
                "API": "GitHub - Branches",
                "Description": "Manage repository branches",
                "Auth": "apiKey",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://api.github.com/repos/{owner}/{repo}/branches",
                "Category": "Development",
                "SubCategory": "GitHub",
                "Endpoints": [
                    "GET /repos/{owner}/{repo}/branches",
                    "GET /repos/{owner}/{repo}/branches/{branch}",
                    "POST /repos/{owner}/{repo}/git/refs",
                    "DELETE /repos/{owner}/{repo}/git/refs/{ref}"
                ]
            },
            {
                "API": "GitHub - Users",
                "Description": "Get user information and manage authentication",
                "Auth": "apiKey",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://api.github.com/users",
                "Category": "Development",
                "SubCategory": "GitHub",
                "Endpoints": [
                    "GET /user",
                    "GET /users/{username}",
                    "GET /user/repos",
                    "GET /users/{username}/repos",
                    "GET /user/followers",
                    "GET /user/following"
                ]
            },
            {
                "API": "GitHub - Organizations",
                "Description": "Manage organization accounts and teams",
                "Auth": "apiKey",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://api.github.com/orgs",
                "Category": "Development",
                "SubCategory": "GitHub",
                "Endpoints": [
                    "GET /orgs/{org}",
                    "GET /user/orgs",
                    "GET /orgs/{org}/repos",
                    "GET /orgs/{org}/teams",
                    "GET /orgs/{org}/members"
                ]
            },
            {
                "API": "GitHub - Gists",
                "Description": "Create and manage code snippets (gists)",
                "Auth": "apiKey",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://api.github.com/gists",
                "Category": "Development",
                "SubCategory": "GitHub",
                "Endpoints": [
                    "GET /gists",
                    "GET /gists/public",
                    "GET /gists/{gist_id}",
                    "POST /gists",
                    "PATCH /gists/{gist_id}",
                    "DELETE /gists/{gist_id}"
                ]
            },
            {
                "API": "GitHub - Actions",
                "Description": "Manage GitHub Actions workflows and runs",
                "Auth": "apiKey",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://api.github.com/repos/{owner}/{repo}/actions",
                "Category": "Development",
                "SubCategory": "GitHub",
                "Endpoints": [
                    "GET /repos/{owner}/{repo}/actions/workflows",
                    "GET /repos/{owner}/{repo}/actions/runs",
                    "GET /repos/{owner}/{repo}/actions/runs/{run_id}",
                    "POST /repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches"
                ]
            },
            {
                "API": "GitHub - Releases",
                "Description": "Manage repository releases and assets",
                "Auth": "apiKey",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://api.github.com/repos/{owner}/{repo}/releases",
                "Category": "Development",
                "SubCategory": "GitHub",
                "Endpoints": [
                    "GET /repos/{owner}/{repo}/releases",
                    "GET /repos/{owner}/{repo}/releases/latest",
                    "GET /repos/{owner}/{repo}/releases/{release_id}",
                    "POST /repos/{owner}/{repo}/releases",
                    "PATCH /repos/{owner}/{repo}/releases/{release_id}"
                ]
            },
            {
                "API": "GitHub - Search",
                "Description": "Search for repositories, code, issues, and users",
                "Auth": "apiKey",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://api.github.com/search",
                "Category": "Development",
                "SubCategory": "GitHub",
                "Endpoints": [
                    "GET /search/repositories",
                    "GET /search/code",
                    "GET /search/issues",
                    "GET /search/users",
                    "GET /search/commits"
                ]
            },
            {
                "API": "GitHub - Webhooks",
                "Description": "Manage repository webhooks and events",
                "Auth": "apiKey",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://api.github.com/repos/{owner}/{repo}/hooks",
                "Category": "Development",
                "SubCategory": "GitHub",
                "Endpoints": [
                    "GET /repos/{owner}/{repo}/hooks",
                    "GET /repos/{owner}/{repo}/hooks/{hook_id}",
                    "POST /repos/{owner}/{repo}/hooks",
                    "PATCH /repos/{owner}/{repo}/hooks/{hook_id}",
                    "DELETE /repos/{owner}/{repo}/hooks/{hook_id}"
                ]
            },
            {
                "API": "GitHub - Contents",
                "Description": "Access and modify repository contents",
                "Auth": "apiKey",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://api.github.com/repos/{owner}/{repo}/contents",
                "Category": "Development",
                "SubCategory": "GitHub",
                "Endpoints": [
                    "GET /repos/{owner}/{repo}/contents/{path}",
                    "PUT /repos/{owner}/{repo}/contents/{path}",
                    "DELETE /repos/{owner}/{repo}/contents/{path}",
                    "GET /repos/{owner}/{repo}/readme"
                ]
            },
            {
                "API": "GitHub - Notifications",
                "Description": "Manage user notifications",
                "Auth": "apiKey",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://api.github.com/notifications",
                "Category": "Development",
                "SubCategory": "GitHub",
                "Endpoints": [
                    "GET /notifications",
                    "GET /repos/{owner}/{repo}/notifications",
                    "PATCH /notifications/threads/{thread_id}",
                    "PUT /notifications"
                ]
            },
            {
                "API": "GitHub - Projects",
                "Description": "Manage GitHub Projects (project boards)",
                "Auth": "apiKey",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://api.github.com/repos/{owner}/{repo}/projects",
                "Category": "Development",
                "SubCategory": "GitHub",
                "Endpoints": [
                    "GET /repos/{owner}/{repo}/projects",
                    "GET /projects/{project_id}",
                    "POST /repos/{owner}/{repo}/projects",
                    "PATCH /projects/{project_id}"
                ]
            }
        ]
    
    def _load_enriched_apis(self) -> list:
        """
        Load enriched collection of high-quality development APIs
        """
        return [
            # Version Control & Code Hosting
            {
                "API": "GitLab API",
                "Description": "Complete REST API for GitLab repositories, CI/CD, and DevOps",
                "Auth": "apiKey",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://gitlab.com/api/v4",
                "Category": "Development"
            },
            {
                "API": "Bitbucket API",
                "Description": "Bitbucket Cloud REST API for Git repositories and pipelines",
                "Auth": "OAuth",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://api.bitbucket.org/2.0",
                "Category": "Development"
            },
            
            # Package Registries
            {
                "API": "npm Registry",
                "Description": "Access npm package metadata and registry information",
                "Auth": "",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://registry.npmjs.org",
                "Category": "Development"
            },
            {
                "API": "PyPI API",
                "Description": "Python Package Index API for package information",
                "Auth": "",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://pypi.org/pypi",
                "Category": "Development"
            },
            {
                "API": "crates.io API",
                "Description": "Rust package registry API",
                "Auth": "",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://crates.io/api/v1",
                "Category": "Development"
            },
            {
                "API": "Maven Central",
                "Description": "Search and access Maven packages",
                "Auth": "",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://search.maven.org/solrsearch/select",
                "Category": "Development"
            },
            
            # Code Quality & Analysis
            {
                "API": "SonarQube",
                "Description": "Code quality and security analysis platform API",
                "Auth": "apiKey",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://sonarcloud.io/api",
                "Category": "Development"
            },
            {
                "API": "Codacy API",
                "Description": "Automated code reviews and code quality analysis",
                "Auth": "apiKey",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://api.codacy.com",
                "Category": "Development"
            },
            
            # CI/CD & Deployment
            {
                "API": "CircleCI API",
                "Description": "Continuous integration and delivery platform API",
                "Auth": "apiKey",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://circleci.com/api/v2",
                "Category": "Development"
            },
            {
                "API": "Travis CI API",
                "Description": "Continuous integration service API",
                "Auth": "apiKey",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://api.travis-ci.com",
                "Category": "Development"
            },
            {
                "API": "Vercel API",
                "Description": "Frontend deployment and hosting platform API",
                "Auth": "apiKey",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://api.vercel.com",
                "Category": "Development"
            },
            {
                "API": "Netlify API",
                "Description": "Web hosting and serverless backend services API",
                "Auth": "apiKey",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://api.netlify.com/api/v1",
                "Category": "Development"
            },
            
            # Documentation & Knowledge
            {
                "API": "Stack Exchange API",
                "Description": "Access Stack Overflow and Stack Exchange sites data",
                "Auth": "OAuth",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://api.stackexchange.com/2.3",
                "Category": "Development"
            },
            {
                "API": "DevDocs API",
                "Description": "Unified API documentation for developers",
                "Auth": "",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://devdocs.io/docs.json",
                "Category": "Development"
            },
            
            # Container & Cloud
            {
                "API": "Docker Hub API",
                "Description": "Access Docker container images and repositories",
                "Auth": "apiKey",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://hub.docker.com/v2",
                "Category": "Development"
            },
            {
                "API": "Heroku API",
                "Description": "Cloud platform as a service (PaaS) API",
                "Auth": "apiKey",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://api.heroku.com",
                "Category": "Development"
            },
            
            # API Development & Testing
            {
                "API": "Postman API",
                "Description": "Manage Postman collections, environments, and mocks",
                "Auth": "apiKey",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://api.getpostman.com",
                "Category": "Development"
            },
            {
                "API": "Swagger/OpenAPI",
                "Description": "OpenAPI specification for API documentation",
                "Auth": "",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://api.apis.guru/v2",
                "Category": "Development"
            },
            {
                "API": "JSONPlaceholder",
                "Description": "Free fake REST API for testing and prototyping",
                "Auth": "",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://jsonplaceholder.typicode.com",
                "Category": "Development"
            },
            {
                "API": "ReqRes",
                "Description": "Hosted REST API for testing frontend applications",
                "Auth": "",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://reqres.in/api",
                "Category": "Development"
            },
            
            # Code Collaboration
            {
                "API": "Slack API",
                "Description": "Team communication and collaboration platform API",
                "Auth": "OAuth",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://slack.com/api",
                "Category": "Development"
            },
            {
                "API": "Discord API",
                "Description": "Voice, video, and text communication platform API",
                "Auth": "OAuth",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://discord.com/api",
                "Category": "Development"
            },
            
            # Project Management
            {
                "API": "Jira API",
                "Description": "Issue and project tracking software API",
                "Auth": "OAuth",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://developer.atlassian.com/cloud/jira/platform/rest/v3",
                "Category": "Development"
            },
            {
                "API": "Trello API",
                "Description": "Kanban-style project management tool API",
                "Auth": "apiKey",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://api.trello.com/1",
                "Category": "Development"
            },
            {
                "API": "Linear API",
                "Description": "Modern issue tracking and project management API",
                "Auth": "apiKey",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://api.linear.app/graphql",
                "Category": "Development"
            },
            
            # Analytics & Monitoring
            {
                "API": "Google Analytics",
                "Description": "Web analytics and reporting API",
                "Auth": "OAuth",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://www.googleapis.com/analytics/v3",
                "Category": "Development"
            },
            {
                "API": "Sentry API",
                "Description": "Error tracking and performance monitoring API",
                "Auth": "apiKey",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://sentry.io/api/0",
                "Category": "Development"
            },
            
            # Security & Vulnerability
            {
                "API": "CVE Details",
                "Description": "Common Vulnerabilities and Exposures database",
                "Auth": "",
                "HTTPS": True,
                "Cors": "unknown",
                "Link": "https://www.cvedetails.com/api",
                "Category": "Development"
            },
            {
                "API": "Snyk API",
                "Description": "Security vulnerability scanning for dependencies",
                "Auth": "apiKey",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://api.snyk.io/v1",
                "Category": "Development"
            },
            
            # Utilities & Tools
            {
                "API": "REST Countries",
                "Description": "Get country information via REST API",
                "Auth": "",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://restcountries.com/v3.1",
                "Category": "Development"
            },
            {
                "API": "IP API",
                "Description": "IP address geolocation API",
                "Auth": "",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://ipapi.co/json",
                "Category": "Development"
            },
            {
                "API": "QR Code Generator",
                "Description": "Generate QR codes via API",
                "Auth": "",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://api.qrserver.com/v1",
                "Category": "Development"
            },
            {
                "API": "UUID Generator",
                "Description": "Generate UUIDs via API",
                "Auth": "",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://www.uuidgenerator.net/api",
                "Category": "Development"
            },
            
            # AI & Machine Learning
            {
                "API": "OpenAI API",
                "Description": "Access GPT models and AI capabilities",
                "Auth": "apiKey",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://api.openai.com/v1",
                "Category": "Development"
            },
            {
                "API": "Hugging Face API",
                "Description": "Access ML models and datasets",
                "Auth": "apiKey",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://api-inference.huggingface.co",
                "Category": "Development"
            },
            
            # Data & Database
            {
                "API": "JSONbin.io",
                "Description": "JSON storage and retrieval service",
                "Auth": "apiKey",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://api.jsonbin.io/v3",
                "Category": "Development"
            },
            {
                "API": "Supabase API",
                "Description": "Open source Firebase alternative with Postgres database",
                "Auth": "apiKey",
                "HTTPS": True,
                "Cors": "yes",
                "Link": "https://supabase.com/docs/reference/api",
                "Category": "Development"
            }
        ]
    
    async def get_github_endpoints(self, search: str = None) -> list:
        """
        Get GitHub REST API endpoints
        
        Args:
            search: Optional search term to filter endpoints
            
        Returns:
            List of GitHub API endpoints
        """
        endpoints = self._github_api_endpoints
        
        if search:
            search_lower = search.lower()
            endpoints = [
                e for e in endpoints
                if search_lower in e["API"].lower()
                or search_lower in e["Description"].lower()
                or search_lower in e.get("SubCategory", "").lower()
            ]
        
        logger.info(f"Returning {len(endpoints)} GitHub API endpoints")
        return endpoints
    
    async def get_enriched_apis(
        self,
        search: str = None,
        auth: str = None,
        limit: int = 100
    ) -> list:
        """
        Get enriched collection of development APIs
        
        Args:
            search: Optional search term
            auth: Optional auth type filter
            limit: Maximum results to return
            
        Returns:
            List of enriched API entries
        """
        apis = self._enriched_apis
        
        if search:
            search_lower = search.lower()
            apis = [
                a for a in apis
                if search_lower in a["API"].lower()
                or search_lower in a["Description"].lower()
            ]
        
        if auth:
            apis = [a for a in apis if a.get("Auth") == auth]
        
        apis = apis[:limit]
        
        logger.info(f"Returning {len(apis)} enriched APIs")
        return apis
    
    async def get_all_curated_apis(
        self,
        include_github: bool = True,
        include_enriched: bool = True,
        search: str = None,
        limit: int = 200
    ) -> list:
        """
        Get all curated APIs (GitHub + enriched)
        
        Args:
            include_github: Include GitHub endpoints
            include_enriched: Include enriched APIs
            search: Optional search term
            limit: Maximum results to return
            
        Returns:
            Combined list of all curated APIs
        """
        all_apis = []
        
        if include_github:
            github_apis = await self.get_github_endpoints(search=search)
            all_apis.extend(github_apis)
        
        if include_enriched:
            enriched_apis = await self.get_enriched_apis(search=search)
            all_apis.extend(enriched_apis)
        
        all_apis = all_apis[:limit]
        
        logger.info(f"Returning {len(all_apis)} total curated APIs")
        return all_apis
    
    async def health_check(self) -> str:
        """Health check for the service"""
        return "healthy"
