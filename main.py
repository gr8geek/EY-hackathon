import os
import urllib.request

from requests.sessions import session
from app import app
from flask import Flask, json, request, redirect, jsonify,render_template
from werkzeug.utils import secure_filename
import compare as comp
from resume_parser import resumeparse
import modelprep as mp
import numpy as np
#data = resumeparse.read_file('Web_Developer_Resume_1.pdf')
from zipfile import ZipFile

ALLOWED_EXTENSIONS = set(['txt', 'pdf'])

store = {} # Single store only allowed for now
'''
store  ---- 
	* jdfile : jdfile content (text)
	* Resume Names : List 
'''
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/zipupload', methods=['POST'])
def upload_file_zip():
	# check if the post request has the file part
	#print("*****Alpha*******")
	
	#print(request.form['alpha'])
	#if 'file' not in request.files:
	#	resp = jsonify({'message' : 'No file part in the request'})
	#	resp.status_code = 400
	#	return resp
	file = request.form['file']
	'''
	if file.filename == '':
		print(file.filename,"-----File Name-----")
		resp = jsonify({'message' : 'No file selected for uploading'})
		resp.status_code = 400
		return resp

	'''
	if file!='':
		#print(request.text)
		#JD = 
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		data = resumeparse.read_file(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		resSkillsEmbedding,skillsName = comp.extractSkillstoVec(data,mp.new_model)
		#jddata = request.form['JD']
		#JDSkills,skills = comp.JDtotxt(jddata,mp.new_model)
		resp = jsonify({'Skills':skills})
		resp.status_code = 201
		return resp
	else:
		resp = jsonify({'message' : 'Allowed file types are txt, pdf'})
		resp.status_code = 400
		return resp
#
@app.route('/jdupload', methods=['POST'])
def upload_jd():
	file = request.files['file']
	if file!='':
		#print(request.text)
		#JD = 
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		data = resumeparse.read_file(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		resSkillsEmbedding,skillsName = comp.extractSkillstoVec(data,mp.new_model)
		#resp = jsonify({'Skills':resSkills})
		#print(resSkillsEmbedding)
		arr = []
		for i in resSkillsEmbedding:
			arr.append(i.tolist())
		jsonString = json.dumps(arr)
		print("Length-------------------------",len(arr))
		resp = jsonify({"skillsvec":jsonString,"skillsname":skillsName})
		return resp
	else:
		resp = jsonify({'message' : 'Allowed file types are txt, pdf'})
		resp.status_code = 400
		return resp


@app.route('/computessingle', methods=['POST'])
def compute():
	# check if the post request has the file part
	print("*****Alpha*******")
	print(request.form['JD'])
	#print(request.form['alpha'])
	file = request.files['file']
	if file.filename!='':
		#print(request.text)
		#JD = 
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		data = resumeparse.read_file(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		resSkills,_ = comp.extractSkillstoVec(data,mp.new_model)
		skillsalpha = request.form['skillsalpha']
		skillsvec = request.form['skillsvec']
		print(skillsalpha)
		#skv = request.form['skv']
		#print(skv)
		#skv = np.array(list(map(int,skv.split(','))))
		#skv = skv.reshape((1,len(skv)))
		#ans = comp.rankScore(np.array(resSkills),np.array(JDSkills),np.array(skv))
		print("Answer ::",ans)

		resp = jsonify({'Rank':float(ans)})
		resp.status_code = 201
		return resp
	else:

		resp = jsonify({'message' : 'Allowed file types are txt, pdf'})
		resp.status_code = 400
		return resp
@app.route("/submit",methods=["POST","GET"])
def submission():
	print(request.files["file"])
	file = request.files["file"]
	file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
	return "<h1>Hello</h1>"

@app.route("/submitfiles",methods = ["POST","GET"])
def submitfiles():
	file = request.files
	file_names = file.keys()
	for i in file_names():
		file1 = request.files[i]
		file1.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
	resp = jsonify({})
	resp.status_code = 200
	return resp

@app.route('/',methods=['GET'])
def home():
   #return render_template('index.html')
   #file = open('')
   return render_template('index.html')

@app.route('/',methods = ["DELETE"])
def clearStoreage():
	store = {}



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
