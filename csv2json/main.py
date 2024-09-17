import os

from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename

from modules.module import allowed_file, csv_to_json, delete_files

UPLOAD_FOLDER = "."

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/convert", methods=["GET", "POST"])
def convert():
    delete_files()
    if request.method == "POST":
        try:
            new_file = request.files.get("file")
            file_name = secure_filename(new_file.filename)
            if allowed_file(file_name):
                new_file.save(os.path.join(app.config["UPLOAD_FOLDER"], file_name))
                csv_to_json(file_name)
                return {"file": file_name[:-3] + "json"}
            else:
                raise ValueError
        except Exception as e:
            return {"error": "Incorrect filename extension"}


@app.route("/<path:filename>", methods=["GET"])
def download(filename):
    return send_from_directory(
        app.config["UPLOAD_FOLDER"], filename, as_attachment=True
    )


if __name__ == "__main__":
    app.run("localhost", 8000)
