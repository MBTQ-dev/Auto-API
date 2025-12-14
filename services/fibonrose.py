"""
Fibonrose Service - Reputation and Logging system for MBTQ Universe
"""

from datetime import datetime
from typing import List, Dict, Any, Optional
import uuid
import logging

logger = logging.getLogger(__name__)


class FibonroseService:
    """
    Fibonrose reputation and logging service
    Tracks user actions and manages reputation scores
    """
    
    # Reputation impact for different actions
    REPUTATION_IMPACTS = {
        "auth_success": 5,
        "code_generation_started": 10,
        "code_generation_completed": 20,
        "deployment_started": 15,
        "deployment_completed": 50,
        "api_entries_fetched": 1,
        "auth_error": -5,
        "code_generation_error": -10,
        "deployment_error": -25
    }
    
    def __init__(self):
        self.logs: List[Dict] = []  # In-memory log storage (use database in production)
        self.reputation: Dict[str, Dict] = {}  # In-memory reputation storage
    
    async def health_check(self) -> str:
        """Check if Fibonrose service is healthy"""
        return "healthy"
    
    async def log_event(
        self, 
        action: str, 
        metadata: Dict[str, Any], 
        user: str
    ) -> Dict:
        """
        Log an event to Fibonrose
        """
        try:
            log_id = str(uuid.uuid4())
            reputation_impact = self.REPUTATION_IMPACTS.get(action, 0)
            
            log_entry = {
                "id": log_id,
                "action": action,
                "metadata": metadata,
                "user": user,
                "timestamp": datetime.utcnow().isoformat(),
                "reputation_impact": reputation_impact
            }
            
            self.logs.append(log_entry)
            
            # Update user reputation
            if user != "system":
                await self._update_reputation(user, reputation_impact, action)
            
            logger.info(f"🌹 Fibonrose: Logged {action} for user {user}")
            
            return log_entry
            
        except Exception as e:
            logger.error(f"Fibonrose logging error: {str(e)}")
            raise
    
    async def _update_reputation(self, username: str, impact: int, action: str):
        """
        Update user's reputation score
        """
        if username not in self.reputation:
            self.reputation[username] = {
                "username": username,
                "score": 0,
                "level": "Novice",
                "total_actions": 0,
                "last_activity": datetime.utcnow().isoformat(),
                "history": []
            }
        
        rep = self.reputation[username]
        rep["score"] += impact
        rep["total_actions"] += 1
        rep["last_activity"] = datetime.utcnow().isoformat()
        rep["history"].append({
            "action": action,
            "impact": impact,
            "timestamp": datetime.utcnow().isoformat()
        })
        
        # Update level based on score
        rep["level"] = self._calculate_level(rep["score"])
        
        logger.info(f"🌹 Fibonrose: Updated reputation for {username} - Score: {rep['score']}, Level: {rep['level']}")
    
    def _calculate_level(self, score: int) -> str:
        """
        Calculate user level based on reputation score
        """
        if score < 50:
            return "Novice"
        elif score < 150:
            return "Apprentice"
        elif score < 300:
            return "Adept"
        elif score < 500:
            return "Expert"
        elif score < 1000:
            return "Master"
        else:
            return "Grandmaster"
    
    async def get_user_logs(
        self, 
        username: str, 
        limit: int = 50
    ) -> List[Dict]:
        """
        Get logs for a specific user
        """
        user_logs = [
            log for log in self.logs 
            if log["user"] == username
        ]
        
        # Sort by timestamp (most recent first)
        user_logs.sort(key=lambda x: x["timestamp"], reverse=True)
        
        return user_logs[:limit]
    
    async def get_reputation(self, username: str) -> Dict:
        """
        Get reputation information for a user
        """
        if username not in self.reputation:
            return {
                "username": username,
                "score": 0,
                "level": "Novice",
                "total_actions": 0,
                "last_activity": None
            }
        
        rep = self.reputation[username].copy()
        # Don't include full history in response
        if "history" in rep:
            rep["recent_history"] = rep["history"][-10:]  # Last 10 actions
            del rep["history"]
        
        return rep
    
    async def get_leaderboard(self, limit: int = 10) -> List[Dict]:
        """
        Get top users by reputation score
        """
        leaderboard = sorted(
            self.reputation.values(),
            key=lambda x: x["score"],
            reverse=True
        )[:limit]
        
        # Clean up for response
        return [
            {
                "username": u["username"],
                "score": u["score"],
                "level": u["level"],
                "total_actions": u["total_actions"]
            }
            for u in leaderboard
        ]
    
    async def get_all_logs(self, limit: int = 100) -> List[Dict]:
        """
        Get all logs (admin function)
        """
        logs = sorted(self.logs, key=lambda x: x["timestamp"], reverse=True)
        return logs[:limit]
