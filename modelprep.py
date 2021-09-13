import re
from gensim.models import Word2Vec
'''
import pandas as pd

def cleanResume(resumeText):
    resumeText = re.sub('http\S+\s*', ' ', resumeText)  # remove URLs
    resumeText = re.sub('RT|cc', ' ', resumeText)  # remove RT and cc
    resumeText = re.sub('#\S+', '', resumeText)  # remove hashtags
    resumeText = re.sub('@\S+', '  ', resumeText)  # remove mentions
    resumeText = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', resumeText)  # remove punctuations
    resumeText = re.sub(r'[^\x00-\x7f]',r' ', resumeText) 
    resumeText = re.sub('\s+', ' ', resumeText)  # remove extra whitespace
    return resumeText

data = pd.read_csv('UpdatedResumeDataSet.csv')
data['cleaned_resume'] = data.Resume.apply(lambda x: cleanResume(x))
data.head()

sent = []
for i in data['cleaned_resume']:
  sent.append(i.split(' '))
print()
model = Word2Vec(sent, min_count=1)
print(model)
words = list(model.wv.vocab)
print(words)
print(model[ 'Python' ])
model.save( ' model.bin ' )


'''

new_model = Word2Vec.load( '_model.bin_' )
def retrainModel(model,JD):
    sent = []
    JD = JD.replace(',',' ')
    JD = JD.replace('.',' ')
    JD = JD.split('.')

    for i in JD:
        sent.append(i.split())
    model.train(sent)
    return model
    # updating the model
    


def getModel():
    return new_model