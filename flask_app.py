
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import send_file
from src.abr import main as abr_main

import os
from flask import flash, request, redirect, url_for
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.debug = True

UPLOAD_FOLDER = '/tmp/uploads'
ALLOWED_EXTENSIONS = {'txt'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def hello_world():
    return 'Hello, welcome to this service!\n use /text'


@app.route('/text2')
def create_from_text():
	    print("salam")
	    abr_main("google gggggg")
	    return send_file('out/text.png', mimetype='image/png')




def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/text', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            text = file.read().decode("utf-8")
            print("\n" * 2 + text + "\n" * 2 )
            abr_main(text)
            return send_file('out/text.png', mimetype='image/png')

            #filename = secure_filename(file.filename)
            #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #return redirect(url_for('uploaded_file',
            #                        filename=filename))


    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
