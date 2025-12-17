"""Health check routes."""
from fastapi import APIRouter
from typing import Dict, Any

from src.controllers.health_controller import HealthController

router = APIRouter(prefix="/api/v1", tags=["health"])


@router.get("/health", response_model=Dict[str, Any])
async def health_check():
    """
    Health check endpoint.
    
    Returns:
        Health status information
    """
    return await HealthController.check()

