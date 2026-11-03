from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///table_todo.db"
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

            todo = Todo_Class(title = title, desc = desc)
            db.session.add(todo)
            db.session.commit()

        todoList = Todo_Class.query.all()
        return render_template("index.html", todoList_html = todoList)


if __name__ == "__main__":
    app.run(debug=True)