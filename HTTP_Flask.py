from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("child.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    render_template("http_flask.html")

if __name__ == "__main__":
    app.run(debug=True)
