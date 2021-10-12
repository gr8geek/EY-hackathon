import os
import urllib.request
import json
from requests.sessions import session
from app import app
from flask import Flask, json, request, redirect, jsonify,render_template
from werkzeug.utils import secure_filename
import compare as comp
from resume_parser import resumeparse
import modelprep as mp
import numpy as np
#data = resumeparse.read_file('Web_Developer_Resume_1.pdf')
import zipfile

ALLOWED_EXTENSIONS = set(['txt', 'pdf'])

store = {} # Single store only allowed for now
'''
store  ---- 
	* jdfile : jdfile content (text)
	* Resume Names : List 
'''
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/zipupload', methods=['POST','GET'])
def upload_file_zip():
	file = request.files['file']
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
		path_to_zip_file = os.path.join(app.config['UPLOAD_FOLDER'], filename)
		directory_to_extract_to = os.path.join(os.getcwd(),"zipres")
		with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
			zip_ref.extractall(directory_to_extract_to)

		#data = resumeparse.read_file(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		#resSkillsEmbedding,skillsName = comp.extractSkillstoVec(data,mp.new_model)
		#jddata = request.form['JD']
		#JDSkills,skills = comp.JDtotxt(jddata,mp.new_model)
		resp = jsonify({'Message':"Extracted Successfully"})
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
	#print(request.form['JD'])
	#print(request.form['alpha'])
	file = request.files['file']
	if file.filename!='':
		#print(request.text)
		#JD = 
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		data = resumeparse.read_file(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		resSkills,_ = comp.extractSkillstoVec(data,mp.new_model)
		print(request.form["skillsalpha"])
		print(str(request.form["skillsalpha"]))
		skillsalpha = json.loads(request.form['skillsalpha'])
		skillsvec = json.loads(request.form['skillsvec'])
		print(skillsvec)
		print(skillsalpha)
		#skv = request.form['skv']
		#print(skv)
		#skv = np.array(list(map(int,skv.split(','))))
		skillsalpha = np.array(skillsalpha)
		skv = skillsalpha.reshape((1,len(skillsalpha)))
		ans = comp.rankScore(np.array(resSkills),np.array(skillsvec),skv)
		print("Answer ::",ans)

		#resp = jsonify({'Rank':float(ans)})
		resp = jsonify({'Rank':float(ans)})
		resp.status_code = 201
		return resp
	else:

		resp = jsonify({'message' : 'Allowed file types are txt, pdf'})
		resp.status_code = 400
		return resp


def computeFile(filename,request):

	# To be finished
	print("*****Alpha*******")
	#print(request.form['JD'])
	#print(request.form['alpha'])
	if filename!='':
		#print(request.text)
		#JD = 
		data = resumeparse.read_file(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		resSkills,_ = comp.extractSkillstoVec(data,mp.new_model)
		#print(request.form["skillsalpha"])
		#print(str(request.form["skillsalpha"]))
		skillsalpha = json.loads(request.form['skillsalpha'])
		skillsvec = json.loads(request.form['skillsvec'])
		#print(skillsvec)
		#print(skillsalpha)
		#skv = request.form['skv']
		#print(skv)
		#skv = np.array(list(map(int,skv.split(','))))
		skillsalpha = np.array(skillsalpha)
		skv = skillsalpha.reshape((1,len(skillsalpha)))
		ans = comp.rankScore(np.array(resSkills),np.array(skillsvec),skv)
		return ans

@app.route("/computemultiple",methods=["POST","GET"])
def computeMultiple():
	print("In Function")
	dirs = os.listdir(os.path.join(os.getcwd(),"zipres/res12"))
	#dirs = os.listdir(os.path.join(os.getcwd(),"zipres/"+dirs[0]))
	fileNames = []
	
	ranks = []
	for i in dirs:
		path1 = os.path.join(os.getcwd(),os.path.join("zipres/res12",i))
		fileNames.append(path1)
	for nm in fileNames:
		ans = computeFile(nm,request)
		ranks.append(ans)
	print("!-!-!=-=-=-=-=-=-=-=-=-=-=")
	print(dirs)
	print(ranks)
	res = jsonify({"Message":"Done","Resume":dirs,"Scores":ranks})
	res.status_code = 200
	return res
	



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
