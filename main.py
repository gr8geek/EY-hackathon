import os
import urllib.request
from app import app
from flask import Flask, request, redirect, jsonify,render_template
from werkzeug.utils import secure_filename
import compare as comp
from resume_parser import resumeparse
import modelprep as mp
import numpy as np
#data = resumeparse.read_file('Web_Developer_Resume_1.pdf')

ALLOWED_EXTENSIONS = set(['txt', 'pdf'])

model = None


def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/file-upload', methods=['POST'])
def upload_file():
	# check if the post request has the file part
	#print("*****Alpha*******")
	
	#print(request.form['alpha'])
	if 'file' not in request.files:
		resp = jsonify({'message' : 'No file part in the request'})
		resp.status_code = 400
		return resp
	file = request.files['file']
	if file.filename == '':
		print(file.filename,"-----File Name-----")
		resp = jsonify({'message' : 'No file selected for uploading'})
		resp.status_code = 400
		return resp
	if file and allowed_file(file.filename):
		#print(request.text)
		#JD = 
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		data = resumeparse.read_file(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		resSkills = comp.extractSkillstoVec(data,mp.new_model)
		print(type(resSkills),"============================= Res skills")
		print(resSkills)
		jddata = request.form['JD']
		JDSkills,skills = comp.JDtotxt(jddata,mp.new_model)
		resp = jsonify({'Skills':skills})
		resp.status_code = 201
		return resp
	else:
		resp = jsonify({'message' : 'Allowed file types are txt, pdf'})
		resp.status_code = 400
		return resp


@app.route('/compute', methods=['POST'])
def compute():
	# check if the post request has the file part
	print("*****Alpha*******")
	print(request.form['JD'])
	#print(request.form['alpha'])
	if 'file' not in request.files:
		resp = jsonify({'message' : 'No file part in the request'})
		resp.status_code = 400
		return resp
	file = request.files['file']
	if file.filename == '':
		print(file.filename,"-----File Name-----")
		resp = jsonify({'message' : 'No file selected for uploading'})
		resp.status_code = 400
		return resp
	if file and allowed_file(file.filename):
		#print(request.text)
		#JD = 
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		data = resumeparse.read_file(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		resSkills,_ = comp.extractSkillstoVec(data,mp.new_model)
		#print(type(resSkills),"============================= Res skills")
		print("9999999999999999999999")
		print(len(resSkills))
		print(len(data['skills']))
		print("Shape",np.array(resSkills).shape)
		jddata = request.form['JD']
		JDSkills,skills = comp.JDtotxt(jddata,mp.new_model)
		print("Shape JD",np.array(JDSkills).shape)
		#print(resume_ra)
		skv = request.form['skv']
		print(skv)
		skv = np.array(list(map(int,skv.split(','))))
		skv = skv.reshape((1,len(skv)))
		ans = comp.rankScore(np.array(resSkills),np.array(JDSkills),np.array(skv))
		print("Answer ::",ans)

		resp = jsonify({'Rank':float(ans)})
		resp.status_code = 201
		return resp
	else:

		resp = jsonify({'message' : 'Allowed file types are txt, pdf'})
		resp.status_code = 400
		return resp

@app.route('/',methods=['GET'])
def home():
   #return render_template('index.html')
   #file = open('')
   return render_template('index.html')


#@app.route('/jdtolist', methods=['POST'])
#def upload_file():
	# check if the post request has the file part
		#print(request.text)
	#JD = request.form['JD']

	#resp = jsonify({'SkillsJD' : })
	#resp.status_code = 201
	#return resp
if __name__ == "__main__":
	app.run(port=5600)
