__author__ = "Harsh Fatepuria"
__email__ = "fatepuri@usc.edu"

import re
from glob import iglob
import os
import sys
import json
import math
from numpy.ma.bench import m1
path=sys.argv[1]
newDict={}

classWordCount=[0,0,0,0]

extraWords=["hello", "hey", "about", "and", "are", "eight","fifteen", "fify", "first", "five", "forty", "found", "four","her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his",  "hundred", "inc", "its", "itself","ltd", "made","myself", "name", "nine", "once", "one","our", "ours",  "she", "six", "sixty","someone","ten", "the", "three", "twelve", "twenty", "two", "yourself", "yourselves", "the"]





input_file_syn=open('synpy.txt','r')
newDictSyn = json.loads(input_file_syn.read())
input_file_syn.close()


pathName=['/negative_polarity/truthful_from_Web/','/negative_polarity/deceptive_from_MTurk/','/positive_polarity/truthful_from_TripAdvisor/','/positive_polarity/deceptive_from_MTurk/']

for i in range(0,4):
    fileR=path+pathName[i]
    xx=[]
    for r,d,fi in os.walk(fileR):
        if len(d)>0:
            xx=xx+d
    for foldnum in range(0,len(xx)):
        for filepath in iglob(os.path.join(fileR+xx[foldnum], '*.txt')):
            with open(filepath) as f:
                for line in f:
                    for word in re.findall(r"[\w']+", line):
                        word=word.lower()
                        word=word.replace("'","")
                        if len(word)>2 and word.isdigit()==False and word not in extraWords:
                            classWordCount[i]=classWordCount[i]+1
                            if word in newDict:
                                newDict[word][i] = newDict[word][i]+1
                            else:
                                newDict[word] = [1,1,1,1]
                                newDict[word][i]=2
    
ll=len(newDict)
for word in newDict.keys():
    m1=math.log(float(newDict[word][0]))-math.log(float(classWordCount[0]+ll))
    m2=math.log(float(newDict[word][1]))-math.log(float(classWordCount[1]+ll))
    m3=math.log(float(newDict[word][2]))-math.log(float(classWordCount[2]+ll))
    m4=math.log(float(newDict[word][3]))-math.log(float(classWordCount[3]+ll))
    newDict[word][0]=m1
    newDict[word][1]=m2
    newDict[word][2]=m3
    newDict[word][3]=m4
    if word in newDictSyn:
        for syns in newDictSyn[word]:
            if len(syns)>2 and syns not in newDict:
                newDict[syns] = [1,1,1,1]
                newDict[syns][0]=m1
                newDict[syns][1]=m2
                newDict[syns][2]=m3
                newDict[syns][3]=m4
                
keys=json.dumps(newDict, sort_keys=True)
output_file=open('nbmodel.txt','w')
output_file.write(keys)
output_file.close()

print len(newDict)
print classWordCount