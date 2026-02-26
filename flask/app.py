from flask import Flask, render_template

app = Flask(__name__)
@app.route("/1")
def home():
    return "Hello World!"

@app.route("/2")
def html_basic():
    return render_template("index2.html")

@app.route("/3")
def hrasek():
    return render_template("index3.html")

if __name__ == "__main__":
    app.run()