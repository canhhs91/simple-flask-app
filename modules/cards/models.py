from db import db


class Item(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    position = db.Column(db.Integer, nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('deck.id'), nullable=True)
    created_at = db.Column(
            db.DateTime,
            nullable=False, server_default=db.func.now()
        )
    updated_at = db.Column(
            db.DateTime,
            nullable=False,
            server_default=db.func.now(), onupdate=db.func.now()
        )


class Deck(Item):
    __table_args__ = {'extend_existing': True}
    name = db.Column(db.String(255), nullable=False)


class Card(Item):
    __table_args__ = {'extend_existing': True}
    content = db.Column(db.Text, nullable=False)
