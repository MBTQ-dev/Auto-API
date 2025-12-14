"""
DeafAUTH Service - Authentication service for MBTQ Universe
"""

from datetime import datetime, timedelta
from typing import Optional, Dict
import secrets
import logging

logger = logging.getLogger(__name__)


class DeafAuthService:
    """
    DeafAUTH authentication service
    Handles user authentication and token management
    """
    
    def __init__(self):
        self.tokens: Dict[str, Dict] = {}  # In-memory token storage (use Redis in production)
        self.users: Dict[str, Dict] = {}   # In-memory user storage (use database in production)
        
    async def health_check(self) -> str:
        """Check if DeafAUTH service is healthy"""
        return "healthy"
    
    async def authenticate(self, username: str, password: Optional[str] = None) -> Dict:
        """
        Authenticate user and generate token
        For demo purposes, any username is accepted
        In production, this should validate against a user database
        """
        try:
            # Generate secure token
            token = secrets.token_urlsafe(32)
            expires_at = datetime.utcnow() + timedelta(hours=24)
            
            # Store token
            self.tokens[token] = {
                "username": username,
                "created_at": datetime.utcnow().isoformat(),
                "expires_at": expires_at.isoformat()
            }
            
            # Store or update user
            if username not in self.users:
                self.users[username] = {
                    "username": username,
                    "created_at": datetime.utcnow().isoformat(),
                    "last_login": datetime.utcnow().isoformat()
                }
            else:
                self.users[username]["last_login"] = datetime.utcnow().isoformat()
            
            logger.info(f"DeafAUTH: User {username} authenticated successfully")
            
            return {
                "success": True,
                "token": token,
                "expires_at": expires_at.isoformat()
            }
            
        except Exception as e:
            logger.error(f"DeafAUTH authentication error: {str(e)}")
            return {
                "success": False,
                "error": str(e)
            }
    
    async def verify_token(self, token: str) -> Optional[Dict]:
        """
        Verify token and return user info
        """
        try:
            if token not in self.tokens:
                logger.warning(f"DeafAUTH: Invalid token attempted")
                return None
            
            token_data = self.tokens[token]
            expires_at = datetime.fromisoformat(token_data["expires_at"])
            
            # Check if token is expired
            if datetime.utcnow() > expires_at:
                logger.warning(f"DeafAUTH: Expired token for user {token_data['username']}")
                del self.tokens[token]
                return None
            
            username = token_data["username"]
            user = self.users.get(username)
            
            if not user:
                return None
            
            return {
                "username": username,
                "token": token,
                **user
            }
            
        except Exception as e:
            logger.error(f"DeafAUTH token verification error: {str(e)}")
            return None
    
    async def revoke_token(self, token: str) -> bool:
        """
        Revoke a token
        """
        try:
            if token in self.tokens:
                del self.tokens[token]
                logger.info(f"DeafAUTH: Token revoked")
                return True
            return False
        except Exception as e:
            logger.error(f"DeafAUTH token revocation error: {str(e)}")
            return False
    
    async def get_user(self, username: str) -> Optional[Dict]:
        """
        Get user information
        """
        return self.users.get(username)
