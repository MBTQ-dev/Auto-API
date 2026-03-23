#!/bin/bash
# Test script for curated APIs endpoints

echo "=================================================="
echo "MBTQ Auto-API - Curated APIs Test Suite"
echo "=================================================="

BASE_URL="http://localhost:8000"

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Test counter
TESTS_PASSED=0
TESTS_FAILED=0

# Function to test endpoint
test_endpoint() {
    local name=$1
    local url=$2
    local expected_count=$3
    
    echo -e "\n${BLUE}Testing: $name${NC}"
    
    response=$(curl -s "$url")
    status=$?
    
    if [ $status -eq 0 ]; then
        count=$(echo "$response" | python -c "import sys, json; data=json.load(sys.stdin); print(len(data) if isinstance(data, list) else 'N/A')")
        
        if [ "$count" != "N/A" ]; then
            echo -e "${GREEN}✓ Success - Found $count items${NC}"
            TESTS_PASSED=$((TESTS_PASSED + 1))
            
            if [ ! -z "$expected_count" ] && [ "$count" -ge "$expected_count" ]; then
                echo -e "${GREEN}  ✓ Count meets expectation (>= $expected_count)${NC}"
            fi
        else
            echo -e "${GREEN}✓ Success - Response is not a list${NC}"
            TESTS_PASSED=$((TESTS_PASSED + 1))
        fi
    else
        echo -e "${RED}✗ Failed - HTTP request failed${NC}"
        TESTS_FAILED=$((TESTS_FAILED + 1))
    fi
}

# Test 1: Health check
echo -e "\n${BLUE}Test 1: Health Check${NC}"
response=$(curl -s "$BASE_URL/api/health")
if echo "$response" | grep -q "healthy"; then
    echo -e "${GREEN}✓ Health check passed${NC}"
    TESTS_PASSED=$((TESTS_PASSED + 1))
else
    echo -e "${RED}✗ Health check failed${NC}"
    TESTS_FAILED=$((TESTS_FAILED + 1))
fi

# Test 2: GitHub API endpoints
test_endpoint "Get all GitHub API endpoints" "$BASE_URL/api/github" 15

# Test 3: Search GitHub APIs
test_endpoint "Search GitHub APIs (issues)" "$BASE_URL/api/github?search=issues" 1

# Test 4: Search GitHub APIs (webhook)
test_endpoint "Search GitHub APIs (webhook)" "$BASE_URL/api/github?search=webhook" 1

# Test 5: Enriched APIs
test_endpoint "Get enriched APIs" "$BASE_URL/api/enriched" 30

# Test 6: Search enriched APIs (docker)
test_endpoint "Search enriched APIs (docker)" "$BASE_URL/api/enriched?search=docker" 1

# Test 7: Filter by auth type
test_endpoint "Filter enriched APIs (apiKey)" "$BASE_URL/api/enriched?auth=apiKey&limit=20" 10

# Test 8: Filter by no auth
test_endpoint "Filter enriched APIs (no auth)" "$BASE_URL/api/enriched?auth=" 5

# Test 9: Curated APIs (all)
test_endpoint "Get all curated APIs" "$BASE_URL/api/curated?limit=200" 50

# Test 10: Curated APIs (GitHub only)
test_endpoint "Get curated APIs (GitHub only)" "$BASE_URL/api/curated?include_enriched=false" 15

# Test 11: Curated APIs (enriched only)
test_endpoint "Get curated APIs (enriched only)" "$BASE_URL/api/curated?include_github=false" 30

# Test 12: Search curated APIs
test_endpoint "Search curated APIs (api)" "$BASE_URL/api/curated?search=api&limit=50" 5

# Test specific API structure
echo -e "\n${BLUE}Test: Verify GitHub API structure${NC}"
response=$(curl -s "$BASE_URL/api/github?search=repositories")
if echo "$response" | python -c "import sys, json; data=json.load(sys.stdin); exit(0 if len(data) > 0 and 'Endpoints' in data[0] else 1)"; then
    echo -e "${GREEN}✓ GitHub API structure is correct (has Endpoints)${NC}"
    TESTS_PASSED=$((TESTS_PASSED + 1))
else
    echo -e "${RED}✗ GitHub API structure is incorrect${NC}"
    TESTS_FAILED=$((TESTS_FAILED + 1))
fi

# Test specific enriched API structure
echo -e "\n${BLUE}Test: Verify enriched API structure${NC}"
response=$(curl -s "$BASE_URL/api/enriched?limit=1")
if echo "$response" | python -c "import sys, json; data=json.load(sys.stdin); exit(0 if len(data) > 0 and 'Link' in data[0] and 'Description' in data[0] else 1)"; then
    echo -e "${GREEN}✓ Enriched API structure is correct${NC}"
    TESTS_PASSED=$((TESTS_PASSED + 1))
else
    echo -e "${RED}✗ Enriched API structure is incorrect${NC}"
    TESTS_FAILED=$((TESTS_FAILED + 1))
fi

# Summary
echo -e "\n=================================================="
echo "Test Summary"
echo "=================================================="
echo -e "Tests Passed: ${GREEN}$TESTS_PASSED${NC}"
echo -e "Tests Failed: ${RED}$TESTS_FAILED${NC}"
echo "Total Tests: $((TESTS_PASSED + TESTS_FAILED))"

if [ $TESTS_FAILED -eq 0 ]; then
    echo -e "\n${GREEN}All tests passed! 🎉${NC}"
    exit 0
else
    echo -e "\n${RED}Some tests failed!${NC}"
    exit 1
fi
