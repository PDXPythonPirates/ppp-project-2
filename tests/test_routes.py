"""Test app routes."""

from app import app


class TestRoutes:
    """Test all routes."""

    def test_index_route(self):
        response = app.test_client().get("/")

        assert response.status_code == 200
