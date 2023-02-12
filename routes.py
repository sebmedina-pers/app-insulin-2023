from crypt import methods
from flask import render_template, flash, request, url_for, redirect, session

from .app import app
from .models import db, Foods
from .constants import INSULINE_TO_CARB, FOOD_CART

# displays all available foods in the db
@app.route("/", methods=["GET"])
def index():
    foods = Foods.query.all()
    return render_template(
        # "test_db.html", #this shows initial query results
        "index.html",
        foods=foods
    )
# adds foods to cart
@app.route("/add/<int:id>", methods=["GET", "POST"])
def add_food(id):
    food_to_add = Foods.query.get_or_404(id)
    # retain foods in list
    if request.method == "POST":
        FOOD_CART.append(food_to_add)
    flash("Added to Cart Successfully!")
    return redirect(url_for(".index"))

# displays all added foods to display in cart
@app.route("/food_cart", methods=["GET", "POST"])
def food_cart():
    carb_grams_sum, insulin_dosage_sum = 0, 0
    foods_added = FOOD_CART
    insuline_to_carb = INSULINE_TO_CARB["default"]
    for food in foods_added:
        carb_grams_sum += food.carb_grams
        insulin_dose = food.carb_grams * INSULINE_TO_CARB["default"]
        insulin_dosage_sum += insulin_dose
    # TEST#2
    session["insulin_dosage_sum"] = insulin_dosage_sum
    return render_template(
        "food_cart.html",
        foods_added=foods_added,
        insuline_to_carb=insuline_to_carb,
        carb_grams_sum=carb_grams_sum,
        insulin_dosage_sum=insulin_dosage_sum
    )
# deletes food item from cart
@app.route("/delete/<int:id>", methods=["GET", "POST"])
def delete_food(id):
    carb_grams_sum, insulin_dosage_sum = 0, 0
    foods_added = FOOD_CART
    insuline_to_carb = INSULINE_TO_CARB["default"]
    for food_item in FOOD_CART:
        if food_item.id == id:
            FOOD_CART.remove(food_item)
    for food in foods_added:
        carb_grams_sum += food.carb_grams
        insulin_dose = food.carb_grams * INSULINE_TO_CARB["default"]
        insulin_dosage_sum += insulin_dose
    return render_template(
        "food_cart.html",
        foods_added=FOOD_CART,
        insuline_to_carb=insuline_to_carb,
        carb_grams_sum=carb_grams_sum,
        insulin_dosage_sum=insulin_dosage_sum
    )
# # calculates insulin dosage based on selected items in food_cart
# @app.route("/calculate")
# def calculate():
#     # remove all foods from list
#     FOOD_CART.clear()
#     return render_template(
#         "calculate.html"
#     )

# add modal
# @app.route("/modal", methods=["GET", "POST"])
# def modal():
#     # print(request)
#     # print("request method", request.method)
#     # FOOD_CART.clear()
#     insuline_to_carb = INSULINE_TO_CARB["default"]
#     session["test"] = "TEST WORKS"
#     print(session["insulin_dosage_sum"])
#     print(request.form.get("entered_glucose_level"))
#     return render_template(
#         "modal.html",
#         insuline_to_carb=insuline_to_carb,
#         food_cart=FOOD_CART
#     )
#     """TO DO:
#         1. figure out how to select the entered glucose level
#         2. save that in session[] or in a constant that can be transferable
#     """

@app.route("/", methods=["GET", "POST"])
def calculate():
    # print(request.method)
    print(request.form.get("glevel"))
    return render_template(
        "modal.html"
    )

if __name__ == "__main__":
    app.run(host="localhost", port=4999)



"""THIS STUFF WAS INITIAL FOR TRYING"""
# @app.route("/")
# def index():
#     return render_template("index.html")

# with app.app_context():
#     foods = Foods.query.all()

# for food in foods:
#     print(food.carb_grams)

# # adds foods to cart
# @app.route("/add/<int:id>", methods=["GET", "POST"])
# def add_food(id):
#     foods = Foods.query.all()
#     food_to_add = Foods.query.get_or_404(id)
#     # retain foods in list
#     FOOD_CART.append(food_to_add)

#     flash("Added to Cart Successfully!")
#     return redirect(url_for(".index"))
#     # return render_template(
#     #     "index.html",
#     #     food_to_add=food_to_add,
#     #     foods=foods
#     # )