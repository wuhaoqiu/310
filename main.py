# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 14:17:06 2019

chatbot corpus comes from:
https://github.com/gunthercox/chatterbot-corpus

@author: whq672437089
"""


"""
propocess
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
            sub1=subparts[0].rstrip().lstrip()
            qrDict[sub1]=subparts[1].rstrip()
    return qrDict

def pureQuestionsText(qrDict):
    questions=""
    #extract questions and combine them into one text
    for question,response in qrDict.items():
        question=sanitize_questions(question)
        questions=questions+question+' .\n '
    return questions


def generateSentenceTokens(questions):
    import nltk
    sentences=nltk.sent_tokenize(questions)
    return sentences

def sanitize_questions(question):
    sanitized_question = question.translate(str.maketrans('', '', string.punctuation)).rstrip().lstrip()
    return sanitized_question


"""
generate Response
"""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from nltk.stem import WordNetLemmatizer

#for a given sentence,return a lemmatized sentence
def lemTokens(tokens):
    lemmatizer=WordNetLemmatizer()
    return [lemmatizer.lemmatize(token) for token in tokens]

def generateResponse(userInput,sentences,askResponseDict,ql,similarityThredhold=0.7):
    #prevent bad input
    if ((similarityThredhold>1) or (similarityThredhold<0)):
        similarityThredhold=0.5
    sentences.append(userInput)
    #vetorize sentences and userinput for fllowing similarity calculation
    vertorizedSentences=TfidfVectorizer(tokenizer=lemTokens,stop_words='english').fit_transform(sentences)
    vals = cosine_similarity(vertorizedSentences[-1], vertorizedSentences)
    #find index of sentences that has highest similarity with input
    valsWithoutLast=vals[0,:-1]
    idx=np.argmax(valsWithoutLast,axis=0)
    #return response
    if(vals[0][idx]<similarityThredhold):
        robotResponse="Your input keywords donot exist in my knowledge"
        return robotResponse
    else:
        question=ql[idx]
        robotResponse =''+askResponseDict.get(question)
        return robotResponse
    


content=""
with open("corpus.txt") as infile:
    for line in infile:
        content=content+" "+line.lower()
        
qrDict=generateConversationTurnDict(content)
    
pureQuestions=pureQuestionsText(qrDict)
sentenceTokens=generateSentenceTokens(pureQuestions)

ql=[]
for question,response in qrDict.items():
    ql.append(question)

flag=True
print("ROBO: Hello, I am a chatbot. Type Bye to exit")
while(flag==True):
    userInput = input()
    userInput=sanitize_questions(userInput.lower())
    if(userInput!='bye'):
        if(userInput=='thanks' or userInput=='thank you' ):
            flag=False
            print("ROBO: You are welcome..")
        else:
            print("ROBO: "+generateResponse(userInput,sentenceTokens,qrDict,ql))
            sentenceTokens.remove(userInput)
    else:
        flag=False
        print("ROBO: Bye! take care..")
    