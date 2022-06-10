from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import datetime
from flask_mail import Mail


with open('config.json', 'r') as j:
    jvars = json.load(j)["vars"]


app = Flask(__name__)
app.config.update(
    MAIL_SERVER='smtp.mail.yahoo.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USE_TLS=False,
    MAIL_USERNAME=jvars['yahoo_user'],
    MAIL_PASSWORD=jvars['yahoo_pass']

)
mail = Mail(app)
if jvars["local_server"]:
    app.config['SQLALCHEMY_DATABASE_URI'] = jvars["local_uri"]

else:
    app.config['SQLALCHEMY_DATABASE_URI'] = jvars["prod_uri"]

db = SQLAlchemy(app)


class Contact(db.Model):
    # srno	name	email	phone_num	message	date

    srno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=False, nullable=False)
    email = db.Column(db.String(50), unique=False, nullable=False)
    phone_num = db.Column(db.String(15), unique=False, nullable=False)
    message = db.Column(db.String(120), unique=False, nullable=False)
    date = db.Column(db.String(40), unique=False, nullable=True)


@app.route("/")
def index():
    return render_template("index.html", jvar=jvars)


@app.route("/about")
def about():
    return render_template("about.html", jvar=jvars)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get('fname')
        email = request.form.get('fmail')
        phone = request.form.get('fnum')
        message = request.form.get('fmsg')
        date = datetime.now()
        entry = Contact(name=name, email=email, phone_num=phone, message=message, date=date)
        db.session.add(entry)
        db.session.commit()
        mail.send_message("New message from "+name, sender=email, recipients=[jvars['yahoo_user']], body=message)

        # date = req
    # srno	name	email	phone_num	message	date

    return render_template("contact.html", jvar=jvars)


@app.route("/post")
def posts():
    return render_template("post.html", jvar=jvars)


# app.run(debug=True)
if __name__ == "__main__":
    app.run(debug=True, port=8000)
