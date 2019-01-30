# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 16:50:30 2019

@author: whq672437089
"""

#the idea behind how this chatbot response is "document similarity", as this chatbot will 
#measure how user input question is similar to the processed corpus questions.
import string
import nltk
import re

nltk.download('punkt')
nltk.download('wordnet')

def generateConversationTurnDict(inputText):
    #split text to independent conversation turn by usinig "--"
    conversationTurn=re.split(r'-\s+-',inputText)
    #remove empty string in the string list
    conversationTurnWithoutEmpty = list(filter(lambda x: len(x)>1, conversationTurn)) 
    
    qrDict={}
    for turn in conversationTurnWithoutEmpty:
        #divide turn into question and answers
        #first part is question as key,second part is response as value
        subparts=re.split(r'\s+-',turn)
        if(len(subparts)==2):
            qrDict[subparts[0].rstrip().lstrip()]=subparts[1].rstrip()
    return qrDict

def pureQuestionsText(qrDict):
    questions=""
    #extract questions and combine them into one text
    for question,response in qrDict.items():
        questions=questions+question+'.\n'
    return questions

def generateCleanWordsTokens(questions):
    #remove all punctuations from text
    questionsWithoutPunc=questions.translate(str.maketrans('','',string.punctuation))
    words=nltk.word_tokenize(questionsWithoutPunc)
    #remove numbers
    wordsWithoutNum=[i for i in words if i.isalpha()]
    return wordsWithoutNum

def generateSentenceTokens(questions):
    import nltk
    sentences=nltk.sent_tokenize(questions)
    return sentences



   
