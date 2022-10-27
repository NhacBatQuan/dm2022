import string
import re
import math
import json

def preprocessing(a):
    a = re.sub('[^A-Za-z0-9]+','',a)
    a = a.lower()
    word = a.split()
    return a,word
    
def tf(a):
    for i in a:
        a = a.count(word)/len(a)
        return a

def idf(a):
    for word in a:
    
    return a
        
        
data_file = open("../input/yelp-dataset/yelp_academic_dataset_review.json")
data = []
count = 0    
for line in data_file:
    data.append(json.loads(line)['text'])
    count = count+1
    if count ==100:
        preprocess = preprocessing(data[0])
        print(data[0])
        tfidf = tf(preprocess) * idf(preprocess)
        break
data_file.close()