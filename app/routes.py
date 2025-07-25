from flask import Blueprint, render_template, request, redirect, url_for
from bson.objectid import ObjectId

main = Blueprint("main", __name__)

@main.route("/")
def index():
    products = list(main.app.db.products.find())
    return render_template("index.html", products=products)

@main.route("/cart")
def cart():
    cart_items = list(main.app.db.cart.find())
    return render_template("cart.html", cart=cart_items)

@main.route("/add_to_cart/<product_id>")
def add_to_cart(product_id):
    product = main.app.db.products.find_one({"_id": ObjectId(product_id)})
    if product:
        main.app.db.cart.insert_one(product)
    return redirect(url_for("main.cart"))

@main.route("/checkout")
def checkout():
    main.app.db.cart.delete_many({})
    return render_template("checkout.html")
