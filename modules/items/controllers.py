from db import db
from flask import request, jsonify

from .models import Item
from .schemas import ItemCreate


def put():
    data = ItemCreate(**request.json)
    item = Item(**data.model_dump())
    try:
        db.session.add(item)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return {'message': str(e)}, 500
    return {'message': 'Data inserted'}, 201


def get(id):
    item = db.session.get(Item, id)
    if item is None:
        return {'message': 'Item not found'}, 404
    return jsonify({
        "id": item.id,
        "name": item.name,
    }), 200


def all():
    items = db.session.query(Item).all()
    return jsonify([{
        "id": item.id,
        "name": item.name,
        } for item in items]), 200
