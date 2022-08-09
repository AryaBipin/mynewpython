from flask import Flask, redirect,request,render_template,flash,url_for,send_from_directory
import urllib.request
import os
from werkzeug.utils import secure_filename
from PIL import Image,ImageDraw
from waitress import serve 

api = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
api.secret_key = "secret key"
api.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

 

@api.route('/')
def home():
    return render_template('index.html')

@api.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico')
 

@api.route('/upload', methods=['POST'])
def upload_image():
    file = request.files['image']
    print (request.files['image'])
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], "filename.jpg"))
        #print('upload_image filename: ' + filename)
    flash('Image successfully uploaded and displayed below')
    img = Image.open(r"static\uploads\\Adlogo2.png")
    background = Image.open(r"static\uploads\\filename.jpg")
    background.paste(img, (0, 0), img)
    mask = Image.new('L', background.size)
    mask_draw = ImageDraw.Draw(mask)
    width, height = background.size
    mask_draw.ellipse((5, 5, width, height), fill=255)
    background.putalpha(mask)
    background.save(os.path.join(app.config['UPLOAD_FOLDER'], "profile.png"))
    return render_template('index.html')
if __name__ == "__main__":
    #app.run(debug=True,port=5001)
    serve(api, host='0.0.0.0', port=5000)