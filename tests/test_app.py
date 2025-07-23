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
    assert response.json()["tip"] in [
    "Always run 'terraform plan' before 'terraform apply'—unless you like surprises!",
    "Continuous Integration: because 'it works on my machine' isn't enough.",
    "Remember: DevOps is a culture, not just a job title.",
    "If it's not in version control, did it ever really exist?",
    "You can't spell 'automation' without 'auto.' Wait, that was obvious.",
    "Use infrastructure as code. Pets are cute, but we prefer cattle in the cloud!",
    "Monitoring: Because we like to know when things break…immediately.",
    "CI/CD pipelines: Embrace the 'merge, build, test, deploy' Zen cycle."
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