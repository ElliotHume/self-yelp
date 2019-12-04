'''Tokenize a JSON lines dataset with nltk
CODE PROVIDED BY:
    Colin Bernet
    https://thedatafrog.com/en/text-preprocessing-machine-learning-yelp/?fbclid=IwAR3Er-ltRjwtk4fiWXSc60_jmWs6vpJBRQWrn0vyzMmPtophLFHR1DErJkw
'''
import os 
import json
import nltk
import sys 
nltk.download('punkt')

def output_fname(input_fname):
    return os.path.splitext(input_fname)[0] + '_tok.json'
def process_file(fname):
    '''tokenize data in file fname. 
    The output is written to fname_tok.json
    '''
    print('opening', fname)
    ofname = output_fname(fname)
    ifile = open(fname, encoding='utf-8')
    ofile = open(ofname,'w')
    for i, line in enumerate(ifile):
        if i%1000 == 0:
            print(i)       
        # convert the json on this line to a dict
        data = json.loads(line) 
        # extract the review text
        text = data['text']
        # tokenize
        words = nltk.word_tokenize(text)
        # convert all words to lower case 
        words = [word.lower() for word in words]
        # updating JSON and writing to output file
        data['text'] = words
        line = json.dumps(data)
        ofile.write(line+'\n')
    ifile.close()
    ofile.close()


fname = 'Seafood_reviews.json'
results = process_file(fname)
