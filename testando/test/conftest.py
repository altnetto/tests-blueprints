import pytest
from application import create_app


@pytest.fixture
def client():
    app = create_app()

    context = app.app_context()
    context.push()

    yield app.test_client()

    context.pop()