import uuid
from flask import Flask,request         ##After using Flask_Smorest###
from flask_smorest import abort
from db import stores,items

app = Flask(__name__)

#Get all stores
@app.get("/store")   # http://127.0.0.1:5000/store
def get_stores():
    return {"stores" : list(stores.values())}


#Get store_data
@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        abort(404, message= "Store not found")


#Create store
@app.post("/store")
def create_store():
    store_data = request.get_json()
    if "name" not in store_data:
        abort(
            400,
            message = "Bad request. Ensure 'name' is included in the JSON payload. "
        )
    for store in stores.values():
        if store_data["name"] == store["name"]:
            abort(404, meassage= "Store already exists. ")
    store_id = uuid.uuid4().hex  #f86fa7df76sdf9ad6fa8df
    store = {**store_data, "id": store_id}
    stores[store_id] = store
    return store, 201

#Delete store
@app.delete("/store/<string:store_id>")
def delete_store(store_id):
    try:
        del stores[store_id]
        return {"message" : "Store deleted. "}
    except KeyError:
        abort(404, message="Store deleted. ")

#Get all items
@app.get("/item")
def get_all_items():
    return {"items": list(items.values())}

#Get item_data
@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        abort(404, message= "Item not found")

#Create item
@app.post("/item")
def create_item():
    item_data = request.get_json()
    if (
        "price" not in item_data
        or "store_id" not in item_data
        or "name" not in item_data
    ):
        abort(
            404, meassage = "Bad request. Ensure 'price', 'store_id', and 'name' are included in the JSON payload."
        )

    for item in items.values():
        if(
            item_data["name"] == item["name"]
            and item_data["store_id"] == item["store_id"]
        ):
            abort(
                404, meassage="Item Already Exists."
            )

    if item_data["store_id"] not in stores:
        abort(404, message= "Store not found")

    item_id = uuid.uuid4().hex
    item = {**item_data, "id":item_id}
    items[item_id] = item
    return item, 201

#Delete item
@app.delete("/item/<string:item_id>")
def delete_item(item_id):
    try:
        del items[item_id]
        return {"message": "Item deleted"}
    except KeyError:
        abort(404, message= "Item not found.")
        
#Update item
@app.put("/item/<string:item_id>")
def update_item(item_id):
    item_data = request.get_json()
    if( "price" not in item_data
        or "name" not in item_data
    ):
        abort(400, message="Ensure 'price' and 'name' are included in the JSON payload. ")

    try :
        item = items[item_id]
        item |= item_data
        return item
    except KeyError:
        abort(404, message="Item not found. ")





