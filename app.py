from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://naeem:Navjivan@localhost/cleanblog'
db = SQLAlchemy(app)


class Contacts(db.Model):
    # srno	name	email	phone_num	message	date
    srno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=False, nullable=False)
    email = db.Column(db.String(50), unique=False, nullable=False)
    phone_num = db.Column(db.String(15), unique=False, nullable=False)
    message = db.Column(db.String(120), unique=False, nullable=False)
    date = db.Column(db.String(40), unique=False, nullable=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get('fname')
        email = request.form.get('fmail')
        phone = request.form.get('fnum')
        message = request.form.get('fmsg')

        entry = Contacts(name=name, email=email, phone_num=phone, message=message)
        db.session.add(entry)
        db.session.commit()
        # date = req
    # srno	name	email	phone_num	message	date

    return render_template("contact.html")


@app.route("/post")
def posts():
    return render_template("post.html")


# app.run(debug=True)
if __name__ == "__main__":
    app.run(debug=True, port=8000)
