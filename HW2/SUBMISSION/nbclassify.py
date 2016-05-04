
__author__ = "Harsh Fatepuria"
__email__ = "fatepuri@usc.edu"

import re
from glob import iglob
import os
import sys
import json
import math

path=sys.argv[1]

input_file=open('nbmodel.txt','r')
newDict = json.loads(input_file.read())
input_file.close()


output_file=open('nboutput.txt','w')

for r,d,fi in os.walk(path):
    if len(d)>=1:
        path=path+"/"+str(d[0])
#print path

fileR=path
#fileR=str(path)+'/both_polarity/deceptive_and_truthful/fold1/'

#print path

keyL=newDict
for filepath in iglob(os.path.join(fileR, '*.txt')): 
    with open(filepath) as f:
        c1=math.log10(0.25)
        c2=math.log10(0.25)
        c3=math.log10(0.25)
        c4=math.log10(0.25)
        for line in f:
            #line="This hotel is the best wors hotel ever."
            for word in re.findall(r'\b[^\W\d_]+\b', line):
                word=word.lower()
                if len(word)>2  and word in keyL:
                    c1=c1+float(newDict[word][0])
                    c2=c2+float(newDict[word][1])
                    c3=c3+float(newDict[word][2])
                    c4=c4+float(newDict[word][3])
        m=max(c1,c2,c3,c4)
        if m==c1:
            s= 'truthful negative '+filepath
        elif m==c2:
            s= 'deceptive negative '+filepath
        elif m==c3:
            s= 'truthful positive '+filepath
        elif m==c4:
            s= 'deceptive positive '+filepath
        print s
        output_file.write(s+"\n");
        



'''


import re
from glob import iglob
import os
import sys
import json
import math
path=sys.argv[1]


input_file=open('nbmodel.txt','r')
newDict = json.loads(input_file.read())
input_file.close()

output_file=open('nboutput.txt','w')

pathName=['/negative_polarity/truthful_from_Web/fold1/','/negative_polarity/deceptive_from_MTurk/fold1/','/positive_polarity/truthful_from_TripAdvisor/fold1/','/positive_polarity/deceptive_from_MTurk/fold1/']
# print [name for name in os.listdir(".") if os.path.isdir(name)]

for i in range(0,4):
    fileR=path+pathName[i]
    for filepath in iglob(os.path.join(fileR, '*.txt')): 
        with open(filepath) as f:
            c1=math.log10(0.25)
            c2=math.log10(0.25)
            c3=math.log10(0.25)
            c4=math.log10(0.25)
            for line in f:
                for word in re.findall(r'\b[^\W\d_]+\b', line):
                #for word in re.findall(r"[\w']+", line):
                    word=word.lower()
                    if len(word)>2 and word in newDict.keys():
                        c1=c1+math.log10(float(newDict[word][0]))-math.log10(float(newDict['a'][0]+len(newDict)-1))
                        c2=c2+math.log10(float(newDict[word][1]))-math.log10(float(newDict['a'][1]+len(newDict)-1))
                        c3=c3+math.log10(float(newDict[word][2]))-math.log10(float(newDict['a'][2]+len(newDict)-1))
                        c4=c4+math.log10(float(newDict[word][3]))-math.log10(float(newDict['a'][3]+len(newDict)-1))
        m=max(c1,c2,c3,c4)
        #print c1,c2,c3,c4,
        if m==c1:
            s= 'truthful negative '+filepath
        elif m==c2:
            s= 'deceptive negative '+filepath
        elif m==c3:
            s= 'truthful positive '+filepath
        elif m==c4:
            s= 'deceptive positive '+filepath
        print s
        output_file.write(s+"\n");
                                
output_file.close()



'''
