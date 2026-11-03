from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Database ka configuration (3 slashes for Windows local path)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///store.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 🌟 DATABASE MODEL (Table ka structure)
class StoreItem(db.Model):
    # Unique ID jo automatic badhegi (1, 2, 3...)
    item_id = db.Column(db.Integer, primary_key=True)
    # Item ka naam store karne ke liye text field
    item_name = db.Column(db.String(200), nullable=False)
    # Item ki price store karne ke liye Integer field (Number)
    item_price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"{self.item_id} - {self.item_name} - Rs.{self.item_price}"


# 🌟 DASHBOARD ROUTE (GET aur POST dono handles karega)
@app.route("/dashboard", methods=["GET", "POST"])
def manage_dashboard_items():
    # Agar user ne form fill karke submit button dabaya hai
    if request.method == "POST":
        # HTML form ke input fields se data unke 'name' attribute ke zariye uthaya
        captured_item_name = request.form.get("form_item_name")
        captured_item_price = request.form.get("form_item_price")

        # Check kiya ki dono fields me user ne kuch likha hai ya nahi
        if captured_item_name and captured_item_price:
            # Database Model ka ek naya object banaya aur usme data fill kiya
            # (Note: Python variable = Table Column Name)
            new_item_object = StoreItem(
                item_name = captured_item_name, 
                item_price = int(captured_item_price) # Price ko string se number me convert kiya
            )
            
            # Flask session me object ko add kiya (Line me lagaya)
            db.session.add(new_item_object)
            # Permanent save kiya database file me brackets () ke sath
            db.session.commit()

    # Chahe data POST hua ho ya normal page khula ho (GET), hum hamesha
    # database se saare items ki list nikaal kar table me dikhane ke liye bhejenge
    all_saved_items = StoreItem.query.all()

    # HTML page render kiya aur database ki list usme bhej di
    return render_template("dashboard.html", html_items_list = all_saved_items)

if __name__ == "__main__":
    app.run(debug=True)
