from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
# 1. 🌟 Sabse upar timezone aur datetime ko import kijiye, mai nya column add kar rhi hun db create hone ke baad => Database Migration
from datetime import datetime, timezone

app = Flask(__name__)
# Hamari database file ka naam 'store.db' hoga
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///store.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 🌟 DATABASE MODEL (Table ka structure)
class StoreItem(db.Model):
    item_id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(200), nullable=False)
    item_price = db.Column(db.Integer, nullable=False)
    # 2. 🌟 Naya Column jodiye (Bina kisi cut/deprecation warning ke)
    date_added = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f"{self.item_id} - {self.item_name} - Rs.{self.item_price}"


# 🌟 ROUTE 1: HOME PAGE ("/")
# Jab user pehli baar website kholega, toh use ye page dikhega jahan login ya dashboard par jaane ka link hoga.
@app.route("/")
def home_page():
    return render_template("index.html")


# 🌟 ROUTE 2: DASHBOARD PAGE ("/dashboard")
# Yeh page form ka data submit (POST) bhi karega aur table ko dikhayega (GET)
@app.route("/dashboard", methods=["GET", "POST"])
def manage_dashboard_items():
    # Agar user ne dashboard page par form submit kiya
    if request.method == "POST":
        captured_item_name = request.form.get("form_item_name")
        captured_item_price = request.form.get("form_item_price")

        if captured_item_name and captured_item_price:
            # Naya item database me save kar rahe hain
            new_item_object = StoreItem(
                item_name = captured_item_name, 
                item_price = int(captured_item_price)
            )
            db.session.add(new_item_object)
            db.session.commit() # Permanently brackets () ke sath save kiya

    # Chahe naya data add hua ho ya normal page khula ho, hum hamesha
    # database se saare items utha kar HTML ko bhejenge dikhane ke liye
    all_saved_items = StoreItem.query.all()
    return render_template("dashboard.html", html_items_list = all_saved_items)

if __name__ == "__main__":
    app.run(debug=True)
