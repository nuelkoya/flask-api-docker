import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_homepage(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Add" in response.data


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert b"<p>OK!</p>" in response.data


def test_watch(client):
    response = client.get("/watch")
    assert response.status_code == 200
    assert b"<p>Docker Watch in Action (make some changes)</p>" in response.data

def test_submit_data_get(client):
    response = client.get("/submit_data")

    assert response.status_code == 200
    assert b"Add" in response.data


def test_submit_data_post(client, monkeypatch):
    called = {}
    def fake_add_text_to_db(fav_food):
        called['fav_food'] = fav_food

    monkeypatch.setattr("app.add_text_to_db", fake_add_text_to_db)

    response = client.post("/submit_data", data={"fav_food": "Bread"})
    assert response.status_code == 200
    assert b"Bread" in response.data
    assert called['fav_food'] == "Bread"

