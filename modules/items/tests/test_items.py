import pytest
from app import create_app
from db import db
from ..models import Item


@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    with app.app_context():
        db.create_all()

    yield app

    with app.app_context():
        db.drop_all()


def test_get_items_controller(app):
    with app.test_client() as client:
        response = client.get('/items/')
        assert response.status_code == 200


def test_get_item_controller(app):
    with app.test_client() as client, app.app_context():
        response = client.put('/items/', json={
            "name": "test",
        })
        response = client.get('/items/1')
        assert response.status_code == 200


def test_create_item_controller(app):
    with app.test_client() as client, app.app_context():
        response = client.put('/items/', json={
            "name": "test",
        })
        assert response.status_code == 201
        count = db.session.query(Item).count()
        assert count == 1
