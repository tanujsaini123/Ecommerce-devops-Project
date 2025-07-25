from flask import Blueprint, render_template, redirect, url_for, current_app
from bson.objectid import ObjectId

main = Blueprint("main", __name__)

@main.route("/")
def index():
    products = list(current_app.db.products.find())
    return render_template("index.html", products=products)

@main.route("/cart")
def cart():
    cart_items = list(current_app.db.cart.find())
    return render_template("cart.html", cart=cart_items)

@main.route("/add_to_cart/<product_id>")
def add_to_cart(product_id):
    product = current_app.db.products.find_one({"_id": ObjectId(product_id)})
    if product:
        current_app.db.cart.insert_one(product)
    return redirect(url_for("main.cart"))

@main.route("/checkout")
def checkout():
    current_app.db.cart.delete_many({})
    return render_template("checkout.html")
