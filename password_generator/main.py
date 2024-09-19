from flask import Flask, redirect, render_template, request
from moduls.module import generate_password

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/generator", methods=["POST"])
def generator():
    """Function recieves a POST request, generates a password and returns it
    In case of an error returns a description of the error
    """
    if request.method == "POST":
        try:
            password = generate_password(request.json)
            return password
        except Exception as error:
            return {"error": error.args}
    return redirect("/")


if __name__ == "__main__":
    app.run("localhost", 5000)
    pass
