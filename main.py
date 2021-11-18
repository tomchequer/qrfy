from flask import Flask, url_for, render_template, request, send_file
from flask_cors import CORS

import qrcode

from io import BytesIO

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template('home.html')



@app.errorhandler(404)
def not_found(error):
    return '<p>something went wrong!<p>', 404

@app.route('/', methods=['POST', 'GET'])
def generate_qr_code(text):
    if request.method == 'POST':
        request.url['the_url']
        return 'the_url'
    qr_code_img = qrcode.make(text)
    qr_code_img.save()




if __name__ == "__main__":
    app.run(debug=True)