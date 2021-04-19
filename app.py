from flask import Flask, render_template, request, redirect, url_for, abort, send_from_directory
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 2 # 2MB
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
app.config['UPLOAD_PATH'] = 'uploads'

@app.route('/')
def index():
	files = os.listdir(app.config['UPLOAD_PATH'])
	return render_template('upload.html',upfiles=files)

@app.route('/',methods=['POST'])
def upload_file():
		upload_file=request.files.get('file')
		filename = secure_filename(upload_file.filename)
		if filename !='':
			file_ext = os.path.splitext(filename)[1]
			if file_ext not in app.config['UPLOAD_EXTENSIONS']:
				abort(400)
			path = os.path.join(app.config['UPLOAD_PATH'],filename)
			upload_file.save(path)
		return redirect(url_for('index'))

@app.route('/uploads/<filename>') 
def upload(filename):
	    return send_from_directory(app.config['UPLOAD_PATH'],filename)       

@app.errorhandler(413)
def too_large(e):
	return "file is too large for use",413
if __name__ == '__main__':
	     app.run(debug=True)
