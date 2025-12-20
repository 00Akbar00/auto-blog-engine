"""Health controller for basic service checks."""


class HealthController:
    """Controller for health endpoints."""

    @staticmethod
    async def health_check() -> dict:
        """Return basic health status."""
        return {"status": "ok"}


