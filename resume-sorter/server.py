from flask import Flask, render_template, request, redirect
import aspose.words as aw
from fileinput import filename
from information import info_dict
app = Flask(__name__)
from main import RunThis
file = None


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def receive_data():
    global file
    file = request.files['file']
    file.save(file.filename)
    run = RunThis(file.filename)
    return redirect("data")


@app.route("/data")
def data():
    return render_template("data.html", info=info_dict)


if __name__ == "__main__":
    app.run(debug=True)


