from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    # date_created = db.Column(db.DateTime, default = datetime.utcnow)
    date_created = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f"{self.sno} - {self.title}"

@app.route("/")
def hello():
    todo = Todo(title= "first todo", desc="start studying!")
    db.session.add(todo)
    db.session.commit()
    return render_template("index.html")

@app.route("/show")
def show():
    allTodo = Todo.query.all()
    # print(allTodo)
    return render_template("index.html", all_todo = allTodo)

if __name__ == "__main__":
    app.run(debug=True)