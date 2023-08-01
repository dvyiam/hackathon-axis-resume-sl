from flask import Flask, render_template, request
import aspose.words as aw
from fileinput import filename
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
    return "DONE"


if __name__ == "__main__":
    app.run(debug=True)


