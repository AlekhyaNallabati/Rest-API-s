from db import db


class ItemTags(db.schema):
    __tablename__ = "item_tags"

    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey("items_id"))
    tag_id = db.Column(db.Integer, db.ForeignKey("tag_id"))
