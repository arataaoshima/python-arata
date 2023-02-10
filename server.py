from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('index.html')

@app.route("/<page_name>")
def show_html(page_name):
    page_html = page_name + ".html"
    return render_template(page_html)