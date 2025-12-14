"""
Simple test script for MBTQ Auto-API
"""

import asyncio
import httpx


async def test_api():
    """Test the main API endpoints"""
    base_url = "http://localhost:8000"
    
    async with httpx.AsyncClient() as client:
        # Test root endpoint
        print("Testing root endpoint...")
        response = await client.get(f"{base_url}/")
        print(f"✓ Root: {response.json()['name']}")
        
        # Test health check
        print("\nTesting health check...")
        response = await client.get(f"{base_url}/api/health")
        data = response.json()
        print(f"✓ Health: {data['status']}")
        print(f"  - DeafAUTH: {data['services']['deafauth']}")
        print(f"  - Fibonrose: {data['services']['fibonrose']}")
        print(f"  - PinkSync: {data['services']['pinksync']}")
        
        # Test authentication
        print("\nTesting authentication...")
        response = await client.post(
            f"{base_url}/api/auth/login",
            json={"username": "test_developer"}
        )
        auth_data = response.json()
        print(f"✓ Auth: {auth_data['message']}")
        token = auth_data['token']
        
        # Test code generation
        print("\nTesting code generation...")
        response = await client.post(
            f"{base_url}/api/generate",
            headers={"X-MBTQ-Token": token},
            json={
                "api_name": "Test API",
                "description": "A test API",
                "link": "https://api.test.com",
                "category": "Testing",
                "auth": "apiKey",
                "https": True
            }
        )
        gen_data = response.json()
        print(f"✓ Code Generated: {gen_data['api_name']}")
        print(f"  - Code length: {len(gen_data['code'])} characters")
        
        # Test deployment
        print("\nTesting deployment...")
        response = await client.post(
            f"{base_url}/api/deploy",
            headers={"X-MBTQ-Token": token},
            json={
                "api_name": "Test API",
                "code": gen_data['code']
            }
        )
        deploy_data = response.json()
        print(f"✓ Deployed: {deploy_data['url']}")
        print(f"  - Status: {deploy_data['status']}")
        print(f"  - Logs: {len(deploy_data['logs'])} entries")
        
        # Test reputation
        print("\nTesting Fibonrose reputation...")
        response = await client.get(
            f"{base_url}/api/fibonrose/reputation",
            headers={"X-MBTQ-Token": token}
        )
        rep_data = response.json()
        print(f"✓ Reputation: {rep_data['score']} points")
        print(f"  - Level: {rep_data['level']}")
        print(f"  - Total actions: {rep_data['total_actions']}")
        
        # Test logs
        print("\nTesting Fibonrose logs...")
        response = await client.get(
            f"{base_url}/api/fibonrose/logs?limit=3",
            headers={"X-MBTQ-Token": token}
        )
        logs_data = response.json()
        print(f"✓ Logs retrieved: {len(logs_data['logs'])} entries")
        
        print("\n" + "="*50)
        print("All tests passed! 🎉")
        print("="*50)


if __name__ == "__main__":
    print("MBTQ Auto-API Test Suite")
    print("="*50)
    asyncio.run(test_api())
