from flask import Flask, render_template, url_for, request

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

@app.route("/4")
def ind4():
    text="ahoj palach"
    return render_template("index4.html", message=text)

@app.route("/5")
def ind5():
    image_url = url_for('static', filename='images/log.jpg')
    return render_template("index5.html", image_url=image_url)

@app.route('/6', methods=['GET', 'POST']) # Předání formulářem z HTML do pythonu
def ind6():
    result = None
    if request.method == 'POST':
        number = request.form.get('number', type=int)
        if number is not None:
            result = number + 1 
    return render_template('index6.html', result=result)

if __name__ == "__main__":
    app.run()

