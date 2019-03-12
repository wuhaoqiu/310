# 310 ChatBot A3

### Author: 

Haoqiu Wu

### Logic Introduction: 

This is a simple chatbot program. The most fundamental theory that this program relies on is text similarity. 

The following steps decribe the logic of this program:
* Clean text, including remove punctuation, duplicate whitespace.
* Divide text into multiple independent conversaiton turns.
* Based on such conversation turns, create a dictionary whose key is the question and value is the response.
* Combine only questions, then tokenlizing and lemmatization them.
* Vectorize those sentence tokens and compare the user input with them.
* Find the most similar question and use it as key to retrieve answer from training corpus.
* Output answer/response.

The training corpus used in our project comes from this [Repo](https://github.com/gunthercox/chatterbot-corpus)

### A3 New Feature Introduction

*Add a GUI where user can input through a text input area and read the recent chat history with chatbot
![alt text](https://i0.hdslb.com/bfs/article/3fd2f716d5e0f187f25b14bad26d8e793be04ac9.jpg@1320w_858h.webp)
*Add a new topic about arts so that currently user can discuss about article authors with chatbot

*Current chatbot is able to deal with user misspelling as long as such misspelling is not too confused

*Make use of other existing language tookit including sklearn library and nltk toolkit

*Make this chatbot into production by deploying it on the django server with the ajax communication technique.[AJAX](),[Django.view](),[Django.template]()
### How to use this program:
* Fork it.
* Create virtule environment and then install all dependecies in requirements.txt
* Move into the folder where manage.py exists
* Run from command line `python manage.py runserver`
* Visit [localhost](127.0.0.1:8000/mlmodels/chatbot_page/) in your browser.
* Enjoy chatting



