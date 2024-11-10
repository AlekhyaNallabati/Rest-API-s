import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint,abort
from db import items, stores

blp = Blueprint("items", __name__, description="Operations on items")

@blp.route("/item/<string:item_id>")
class Item(MethodView):
    def get(self, item_id):
        try:
            return items[item_id]
        except KeyError:
            abort(404, message="Item not found")

    def delete(self, item_id):
        try:
            del items[item_id]
            return {"message": "Item deleted"}
        except KeyError:
            abort(404, message="Item not found.")

    def put(self, item_id):
        item_data = request.get_json()
        if ("price" not in item_data
                or "name" not in item_data
        ):
            abort(400, message="Ensure 'price' and 'name' are included in the JSON payload. ")

        try:
            item = items[item_id]
            item |= item_data
            return item
        except KeyError:
            abort(404, message="Item not found. ")


@blp.route("/item")
class ItemList(MethodView):
    def get(self):
        return {"items": list(items.values())}

    def post(self):
        store_data = request.get_json()
        if "name" not in store_data:
            abort(
                400,
                message="Bad request. Ensure 'name' is included in the JSON payload. "
            )
        for store in stores.values():
            if store_data["name"] == store["name"]:
                abort(404, meassage="Store already exists. ")
        store_id = uuid.uuid4().hex  # f86fa7df76sdf9ad6fa8df
        store = {**store_data, "id": store_id}
        stores[store_id] = store
        return store, 201
