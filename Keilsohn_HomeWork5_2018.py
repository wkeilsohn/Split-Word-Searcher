# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 09:24:23 2018

@author: William Keilsohn
"""

#Import Packages
import nltk
import re

#Open the File
## The "data" is from: https://pirateipsum.me/
## I just made a few edits to include some of the special characters we are interested in. 

file = open("testfile.txt", "r")
text = file.read() #https://www.guru99.com/reading-and-writing-files-in-python.html
#print(text)
file.close()


# Question 1:
Q1 = re.findall(r'\S+?[-]+[\\n]\w+|\S+?[-]+[\n]\w+', text)# https://docs.python.org/3/library/re.html
print(Q1) #Answers the first Question
print("\n")#Just makes the answers easier to read.

# Question 2:
answerString1 = ''
for x in Q1:
    answerString1 = answerString1 + x + " "


Q2 = re.sub(r'\\n', '', answerString1)
Q2 = re.sub(r'\n', '', Q2) #Double check for both conditions.
print(Q2) #Answers the second question
print("\n")

# Question 3:
allWords = [w for w in nltk.corpus.words.words('en')] #From ppt.
Q3 = nltk.word_tokenize(Q2)

def wordChecker(lis): #Assumes all words are in English.
    newLis = []
    for x in lis:
        tempWord = re.sub(r'-', '', x)
        if tempWord in allWords: #https://stackoverflow.com/questions/7571635/fastest-way-to-check-if-a-value-exist-in-a-list
            newLis.append(tempWord)
        else:
            newLis.append(x)
    return newLis
print(wordChecker(Q3)) #Answers third question