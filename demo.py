import numpy as np
from resume_parser import resumeparse
'''
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
  JDw = np.array(JDw)
  mat1 = np.outer(resumeParams,JDw)
  score = np.sum(np.sum(mat1))
  print(score,"  score")
  print(score.shape,"     score shape")
  return score


'''
data2 = resumeparse.read_file('jdfile.txt', 'w')
#skills = data2['skills']
print(data2)
