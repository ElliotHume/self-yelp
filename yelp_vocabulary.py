'''
Build the vocabulary for the yelp dataset

USING CODE PROVIDED BY:
    Colin Bernet
    https://thedatafrog.com/en/text-preprocessing-machine-learning-yelp/?fbclid=IwAR3Er-ltRjwtk4fiWXSc60_jmWs6vpJBRQWrn0vyzMmPtophLFHR1DErJkw

Modified by Elliot Hume
'''
import json
from collections import Counter
import os
import glob    
import pprint
from vocabulary import Vocabulary

# stop words are words that occur very frequently,
# and that don't seem to carry information 
# about the quality of the review. 
# we decide to keep 'not', for example, as negation is an important info.
# I also keep ! which I think might be more frequent in negative reviews, and which is 
# typically used to make a statement stronger (in good or in bad). 
# the period, on the other hand, can probably be considered neutral
# this could have been done at a later stage as well, 
# but we can do it here as this stage is fast 
stopwords = set(['.','i','a','and','the','to', 'was', 'it', 'of', 'for', 'in', 'my', 
                 'that', 'so', 'do', 'our', 'the', 'and', ',', 'my', 'in', 'we', 'you', 
                 'are', 'is', 'be', 'me'])
def process_file(fname):
    '''process a review JSLON lines file and count the occurence 
    of each words in all reviews.
    returns the counter, which will be used to find the most frequent words
    '''
    print(fname)
    with open(fname, encoding='utf-8') as ifile:
        counter = Counter()
        for i,line in enumerate(ifile):
            if i%10000==0:
                print(i)            
            data = json.loads(line) 
            # extract what we want
            words = data['text']               
            for word in words:
                # if word in stopwords:
                #     continue
                counter[word]+=1
        return counter

fname = 'Seafood_reviews_tok.json' # input("Filename: ")
results = process_file(fname)
print(results.most_common(200))


vocabulary = Vocabulary(results, n_most_common=10000)
vocabulary.save('index')

pprint.pprint(results.most_common(200))
print(len(results))
print(vocabulary)
os.chdir(olddir) 
