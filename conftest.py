import pytest
import app
from controllers import User


@pytest.fixture
def api():
    client = app.test_client()
    return client
