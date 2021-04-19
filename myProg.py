# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 14:22:45 2021

@author: kamal
"""

import json
from difflib import get_close_matches

data=json.load(open('data.json'))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys())) > 0:
        user_ip =  input("Did you mean %s instead? Enter Y if yes, N if no: " % get_close_matches(w,data.keys())[0])
        if user_ip.lower()=="y":
            return data[get_close_matches(w,data.keys())[0]]
        elif user_ip.lower() == "n":
            return "The word doesn't exist. Please double check it"
        else:
            return "Wrong Input!"
            
    else:
        return "The word doesn't exists. Please search for another word!"

word = input("Enter a word: ")
output = translate(word)

if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)