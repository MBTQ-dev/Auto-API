"""
Configuration for MBTQ Auto-API
"""

from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application settings"""
    
    # Application
    app_name: str = "MBTQ Auto-API"
    app_version: str = "1.0.0"
    debug: bool = False
    
    # Server
    host: str = "0.0.0.0"
    port: int = 8000
    
    # CORS
    cors_origins: list = ["*"]  # In production, specify actual origins
    
    # MBTQ Services
    deafauth_endpoint: Optional[str] = None
    fibonrose_endpoint: Optional[str] = None
    pinksync_endpoint: Optional[str] = None
    
    # API Keys (for external services)
    vercel_token: Optional[str] = None
    github_token: Optional[str] = None
    
    # Token Settings
    token_expiry_hours: int = 24
    
    # Rate Limiting
    rate_limit_per_minute: int = 60
    
    # Logging
    log_level: str = "INFO"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Global settings instance
settings = Settings()
