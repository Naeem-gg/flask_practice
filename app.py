from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import datetime
# from flask_mail import Mail

with open('config.json', 'r') as j:
    jvars = json.load(j)["vars"]

app = Flask(__name__)
# app.config.update(
#     MAIL_SERVER='smtp.mail.yahoo.com',
#     MAIL_PORT=465,
#     MAIL_USE_SSL=True,
#     MAIL_USE_TLS=False,
#     MAIL_USERNAME=jvars['yahoo_user'],
#     MAIL_PASSWORD=jvars['yahoo_pass']

# )
# mail = Mail(app)
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


class Posts(db.Model):
    #  	srno 	title 	slug 	content 	post_by 	date
    srno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=True)
    slug = db.Column(db.String(30), unique=True, nullable=False)
    content = db.Column(db.String(300), unique=False, nullable=False)
    post_by = db.Column(db.String(20), unique=True, nullable=False)
    post_img = db.Column(db.String(30), unique=False)
    tagline = db.Column(db.String(35), unique=False)
    date = db.Column(db.String(20), unique=True, nullable=True)


@app.route("/")
def index():
    posts = Posts.query.filter_by().all()
    return render_template("index.html", jvar=jvars, posts=posts)


@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        return "<h1>Logged in successfully"
    else:
        return render_template("admin.html", jvar=jvars)


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
        # mail.send_message("New message from "+name, sender=email, recipients=[jvars['yahoo_user']], body=message)

        # date = req
    # srno	name	email	phone_num	message	date

    return render_template("contact.html", jvar=jvars)


@app.route("/post/<string:post_slug>", methods=['GET'])
def posts_route(post_slug):

    post = Posts.query.filter_by(slug=post_slug).first()

    return render_template("post.html", jvar=jvars, post=post)


# app.run(debug=True)
if __name__ == "__main__":
    app.run(debug=True, port=8000)
