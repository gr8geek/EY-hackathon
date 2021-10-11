import numpy as np
from resume_parser import resumeparse

coun = 0
def extractSkillstoVec(data,w2v):
  skills = data['skills']
  sk1 = []
  sk2 = []
  for i in skills:
    if len(i.strip().split())==1:
      try:
        #print(i)
        sk2.append(i.strip())
        vec = w2v.wv.__getitem__(i.strip())
        sk1.append(vec)

      except:
        pass
  return sk1,sk2

def rankScore(resumeParams,JDparams,alpha):
  #JDw = JDparams * alpha
  print("=====")
  print(JDparams.shape)
  
  print(alpha.shape)
  JDw = []
  for i in range(0,alpha.shape[1]):
    JDw.append(JDparams[i]*alpha[0][i])
  #JDw = np.array(JDw)
  score = 0
  for i in JDw:
    for j in resumeParams:
      score+= -np.dot(i,j)*np.log(1/np.linalg.norm(i-j))
  
  #mat1 = np.outer(resumeParams,JDw)
  ''''
  print("Resume Params")
  print(resumeParams)
  print("Jdw")
  print(JDw)
  print("-------------_Dim 1-----------------",mat1.shape)
  score = np.sum(np.sum(mat1))
  print(score,"  score")
  print(score.shape,"     score shape")
  '''
  return score

def JDtotxt(JobDesc,model):
  file1 = open('JD'+str(coun)+'.txt', 'w')
  file1.write(JobDesc)
  file1.close()
  data2 = resumeparse.read_file('JD'+str(coun)+'.txt', 'w')
  #skills = data2['skills']
  skillvec,skills = extractSkillstoVec(data2,model)

  return skillvec,skills
  #print(skills)
  #Resume parser is also able to extract skills out of JOB description
  #The same topic modeling algorithim can do 2 different things
    