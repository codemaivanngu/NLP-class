import numpy as np
import pandas as pd
import os
import re
import string 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import random

folder_path = "sherlock/sherlock"
def read_all_text():
    all_text = ""
    for file_name in sorted(os.listdir(folder_path)):
        if file_name.endswith(".txt"):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path,"r") as file:
                s = " ".join(file.readlines())
                all_text += s
                # print(len(all_text))
    return all_text 

def clean_data(text):
    print(text[:1000])
    text = text.lower()
    text = re.sub(r"[,.\"\'!@#$%^&*(){}?/;:~`<>|\\-_+=]","",text)
    tokens = word_tokenize(text=text)
    words = [word for word in tokens if word.isalpha()]
    return words

def create_markov_(words):
    dictionary = {}

    for i in range(len(words)-1):
        if words[i] not in dictionary:
            dictionary[words[i]] = {"__cnt":0}
        if words[i+1] not in dictionary[words[i]]:
            dictionary[words[i]][words[i+1]] = 0
        dictionary[words[i]][words[i+1]]+=1
        dictionary[words[i]]["__cnt"]+=1

    for key_1 in dictionary.keys():
        for key_2 in list(dictionary[key_1].keys())[1:]:
            dictionary[key_1][key_2]/=dictionary[key_1]["__cnt"]
        dictionary[key_1]["__cnt"] = 0
    return dictionary

def next_word(word:str, dictionary:dict):
    if word not in dictionary:
        exit()
    probabilities = list(dictionary[word].values())[1:]
    words = list(dictionary[word].keys())[1:]
    # print(words,probabilities,sum(probabilities))
    return words[np.random.choice(len(words),p=probabilities)]

text = read_all_text()
words = clean_data(text)
dictionary = create_markov_(words=words)
word = ["string"]
for i in range(n_iter := 100 ):
    word.append(next_word(word=word[-1],dictionary=dictionary))
print(" ".join(word))
# print(next_word(word,dictionary))
# print(words[:1000])
# print(len(words))

