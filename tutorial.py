from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello!</h1><h2>Hello!</h2><h3>Hello!</h4>"

# @app.route("/<name>")
# def user(name):
#     return f"<h1>Hello, {name}!</h1><h2>Hello, {name}!</h2><h3>Hello, {name}!</h4>"

# @app.route("/admin")
# def admin():
#     return redirect(url_for("user", name="Admin!"))

if __name__ == "__main__":
    app.run()
