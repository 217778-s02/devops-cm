import os
import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

@pytest.fixture
def set_env_vars():
    os.environ["APP_NAME"] = "Test App"
    os.environ["ENVIRONMENT"] = "test"
    os.environ["SECRET_KEY"] = "test-secret-key"
    yield
    del os.environ["APP_NAME"]
    del os.environ["ENVIRONMENT"]
    del os.environ["SECRET_KEY"]

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "OK", "message": "The application is healthy!"}

def test_get_version():
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json() == {"version": "1.0.0"}

def test_get_env(set_env_vars):
    response = client.get("/env")
    assert response.status_code == 200
    assert response.json() == {
    "app_name": "Test App",
    "environment": "test",
    "secret_key": "test-secret-key"
    }

def test_get_devops_tip():
    response = client.get("/tips")
    assert response.status_code == 200
    assert "tip" in response.json()
    ]

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
    "message": "Welcome to the DevOps Demo App!",
    "available_endpoints": ["/health", "/version", "/env", "/tips"]
    }

def test_login():
    response = client.get("/login")
    assert response.status_code == 200
    assert response.json() == {"status": "authenticated"}

def test_logout():
    response = client.get("/logout")
    assert response.status_code == 200
    assert response.json() == {"status": "logged out"}
