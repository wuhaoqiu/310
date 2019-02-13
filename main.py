# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 14:17:06 2019

chatbot corpus comes from:
https://github.com/gunthercox/chatterbot-corpus

@author: whq672437089
"""
import generateResponse as gr
import preprocess as pp
content=""
with open("corpus.txt") as infile:
    for line in infile:
        content=content+" "+line.lower()
qrDict=pp.generateConversationTurnDict(content)
pureQuestions=pp.pureQuestionsText(qrDict)
sentenceTokens=pp.generateSentenceTokens(pureQuestions)
ql=[]
for question,response in qrDict.items():
    ql.append(question)

flag=True
print("ROBO: Hello, I am a chatbot. Type Bye to exit")
while(flag==True):
    userInput = input()
    userInput=pp.sanitize_questions(userInput.lower())
    if(userInput!='bye'):
        if(userInput=='thanks' or userInput=='thank you' ):
            flag=False
            print("ROBO: You are welcome..")
        else:
            print("ROBO: "+gr.generateResponse(userInput,sentenceTokens,qrDict,ql))
            sentenceTokens.remove(userInput)
    else:
        flag=False
        print("ROBO: Bye! take care..")
    