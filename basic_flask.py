from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route('/home')
def home():
    return "Hello World"

@app.route("/")
def index():
    return render_template("index.html")



@app.route('/<name>')
def user(name):
    # return render_template("index.html", content=name + f"    Hello {name}")
    return render_template("index.html", content=["lst1",2,4.5])



@app.route("/admin")
def admin():
    return redirect(url_for("home"))

# @app.route("/redirect_user")
# def redirect_user():
#     return redirect(url_for("user", name="name_redirect"))


@app.route("/redirect_user/")
def redirect_user():
    return redirect(url_for("user", name="name_redirect_with_slash"))



if __name__ == "__main__":
    app.run(debug=True)

