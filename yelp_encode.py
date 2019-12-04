'''
USING CODE PROVIDED BY:
    Colin Bernet
    https://thedatafrog.com/en/text-preprocessing-machine-learning-yelp/?fbclid=IwAR3Er-ltRjwtk4fiWXSc60_jmWs6vpJBRQWrn0vyzMmPtophLFHR1DErJkw

Modified by Elliot Hume
'''

import json
import os
from collections import Counter
def output_fname(input_fname):
    return  input_fname.split('_')[0] + '_enc.json'
def process_file(fname, vocabulary):
    '''process a review JSON lines file and count the words in all reviews.
    returns the counter, which will be used to find the most frequent words
    '''
    print(fname)
    ofname = output_fname(fname)  
    ifile = open(fname, encoding='utf-8') 
    ofile = open(ofname,'w')
    for i,line in enumerate(ifile):
        if i%10000==0:
            print(i)        
        data = json.loads(line) 
        words = data['text']     
        codes = vocabulary.encode(words)
        data['text'] = codes
        line = json.dumps(data)
        ofile.write(line+'\n')        
    ifile.close()
    ofile.close()
   
from vocabulary import Vocabulary
vocabulary = Vocabulary.load('index')

fname = 'Seafood_reviews_tok.json'
process_file(fname, vocabulary)
