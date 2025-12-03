from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("child.html")

@app.route("/logininfo", methods=["GET", "POST"])
def logininfo():
    if request.method == "GET":
        return render_template("logininfo.html")
    elif request.method == "POST":
        htmlname_loc = request.form["htmlname"]
        return redirect(url_for("methoduser", username=htmlname_loc))
    return None


@app.route("/<username>")
def methoduser(username):
    return f"<h1>{username}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
