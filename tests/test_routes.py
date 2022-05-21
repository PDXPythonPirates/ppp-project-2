"""Test app routes."""

from app import app


class TestRoutes:
    """Test all routes."""

    def test_blank_route(self):
        response = app.test_client().get("/")

        assert response.status_code == 200

    def test_index_route(self):
        response = app.test_client().get("/index")

        assert response.status_code == 200

    def test_login_route(self):
        response = app.test_client().get("/login")

        assert response.status_code == 200

    # def test_logout_route(self):
    #     response = app.test_client().get("/logout")

    #     assert response.status_code == 302

    def test_register_route(self):
        response = app.test_client().get("/register")

        assert response.status_code == 200
