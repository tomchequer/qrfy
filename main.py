from flask import Flask, url_for, render_template



app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')


@app.errorhandler(404)
def not_found(error):
    return '<p>something went wrong!<p>', 404


if __name__ == "__main__":
    app.run(debug=True)