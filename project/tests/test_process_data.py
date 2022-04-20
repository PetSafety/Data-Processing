from project.api.models import DadosEmbarcado
# Third party modules
import pytest

# First party modules
from .. import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_ping(client):
    rv = client.get("/api/ping")

    print(rv.data)
    message = {
        "message": "works!"
        }

    assert eval(rv.data) == message