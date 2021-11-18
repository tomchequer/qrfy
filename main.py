from flask import Flask, url_for, render_template, request, send_file
from flask_cors import CORS

import qrcode

from io import BytesIO, StringIO

from werkzeug.wrappers import response

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template('home.html')



@app.errorhandler(404)
def not_found(error):
    return '<p>something went wrong!<p>', 404

@app.route('/', methods=['POST', 'GET'])
def generate_qr_code():   
    if request.method == 'POST':
        buffer = BytesIO()
        the_url = request.form['the_url']
        
        img = qrcode.make(the_url)
        img.save(buffer)
        buffer.seek(0)
        
        response = send_file(buffer, mimetype='image/png')
        
        return response
    

if __name__ == "__main__":
    app.run(debug=True)