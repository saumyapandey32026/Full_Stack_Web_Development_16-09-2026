from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///table_todo.db"    # table_todo.db => database file name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo_Class(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    # date_created = db.Column(db.DateTime, default = datetime.utcnow)
    date_created = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f"{self.sno} - {self.title}"


    
@app.route("/", methods = ["GET", "POST"])
def show():
        if request.method == "POST":
            # title = request.form['title1']
            title = request.form.get("title1")
            # desc = request.form['desc1']
            desc = request.form.get("desc1")

            todo1 = Todo_Class(title = title, desc = desc)
            db.session.add(todo1)
            db.session.commit()

        todoList = Todo_Class.query.all()
        return render_template("index.html", todoList_html = todoList)

@app.route("/delete/<int:sno>")
def delete(sno):
     todo2 = Todo_Class.query.filter_by(sno=sno).first()
     db.session.delete(todo2)
     db.session.commit()
     return redirect("/")

@app.route("/update/<int:sno>", methods=["GET", "POST"])
def update(sno):
        # Sabse pehle database se woh specific todo fetch karein
            todo3 = Todo_Class.query.filter_by(sno=sno).first_or_404()
     
            if request.method == "POST":
                title = request.form.get("title1")
                desc = request.form.get("desc1")

        # Database mein values update karein
                todo3.title = title
                todo3.desc = desc
        # SQLAlchemy mein update ke liye db.session.add() likhna zaroori nahi hota, sirf commit kaafi hai
                # db.session.add(todo3)
                db.session.commit()  

        # Update hone ke baad redirect karein (Maan lijiye aapka home route ka naam 'home' ya 'index' hai)
                return redirect("/") 
        # Agar GET request hai (yani user ne page pehli baar khola hai), toh form dikhayein
            return render_template("update.html", todo3_html = todo3)
     



if __name__ == "__main__":
    app.run(debug=True)