import pytest
from landpage import create_app


@pytest.fixture(scope="module")
def app():
    app = create_app()
    return app
