
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def naeem():
    return render_template("/first.html")

app.run(debug=True)
