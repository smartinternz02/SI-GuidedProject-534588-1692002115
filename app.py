from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(r"index.html")

@app.route('/category')
def category():
    return render_template(r"category.html")
@app.route('/about')
def about():
    return render_template(r"about.html")
@app.route('/contact')
def contact():
    return render_template(r"contact.html")
if __name__ == "__main__":
    app.run(debug=False, port=5500)