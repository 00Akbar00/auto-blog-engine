"""Health check controller."""
from typing import Dict, Any

from src.utils.logger import get_logger

logger = get_logger(__name__)


class HealthController:
    """Controller for health check endpoints."""
    
    @staticmethod
    async def check() -> Dict[str, Any]:
        """
        Health check endpoint handler.
        
        Returns:
            Dict with health status information
        """
        return {
            "status": "healthy",
            "service": "auto-blog-scraper",
            "version": "1.0.0"
        }

