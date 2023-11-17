import pytest
from fastapi.testclient import TestClient

from database import prepare_db
from main import app


@pytest.fixture(autouse=True)
def prepare_database() -> None:
    """
    Returns database to the initial data
    state after each test.
    """
    prepare_db()


@pytest.fixture(scope="session")
def client() -> TestClient:
    return TestClient(app)
