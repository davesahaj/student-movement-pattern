from flask import Flask, render_template, redirect, url_for
app = Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='template')
app.config["DEBUG"] = True


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route("/home")
def home():
    return render_template("home.html")@app.route("/<name>")


@app.route("/<name>")
def user(name):
    return f"Hello-- {name}!"@app.route("/admin")


@app.route("/admin")
def admin():
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run()
