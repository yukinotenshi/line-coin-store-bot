import os

from flask import Flask, request, jsonify
from model import db, Order
import dotenv

dotenv.load_dotenv()
app = Flask(__name__)


@app.after_request
def close_db(resp):
    if not db.is_closed():
        db.close()

    return resp


@app.before_request
def open_db():
    if db.is_closed():
        db.connect()


@app.route("/", methods=["POST"])
def submit_order():
    headers = request.headers
    if headers['Authorization'] != os.getenv("WEBHOOK_PSWD"):
        return ""

    data = request.json
    data['order_id'] = data['id']
    del data['id']
    del data['status']
    order = Order(**data)
    order.save()

    return jsonify({"success": True})


if __name__ == "__main__":
    app.run()
