'''
Created on Dec 11, 2017

@author: VarunJoshi
'''
import json
import difflib
import logging

jsonobject = json.load(open('data.json', 'r'));
Logger = logging.getLogger()
# create logger with 'spam_application'
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('test.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)
 
def getMeaning(word):
    word = word.lower()
    matches = difflib.get_close_matches(word, jsonobject.keys())
    if word in jsonobject:
        return jsonobject[word]
    elif len(matches) > 0:
        yn = input('Do you mean %s instead? Enter Y for Yes, N for No: '%matches[0])
        if yn == 'Y':
            return jsonobject[matches[0]]
        elif yn == 'N':
             return "No meaning found in dictionary."
        else:
            return "Could not understand your query."  
    else:
        return "No meaning found in dictionary."

iscontinue = ''
while True:
    word = input('Please enter a word : ')
    print(getMeaning(word))
    