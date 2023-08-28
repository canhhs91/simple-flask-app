from db import db


class Item(db.Model):
    __table_args__ = {'extend_existing': True} # This is to avoid the error sqlalchemy.exc.InvalidRequestError: Table 'my_item' is already defined for this MetaData instance.  Specify 'extend_existing=True' to redefine options and columns on an existing Table object.
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
