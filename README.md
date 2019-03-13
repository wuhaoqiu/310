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

![alt text](https://github.com/wuhaoqiu/simple-chatbot/blob/haoqiuwu/screenshots/gui.png)

*Various response returned when the content users input is beyong the scope of chatbot

![alt text](https://github.com/wuhaoqiu/simple-chatbot/blob/haoqiuwu/screenshots/five%20different%20response.png)

*Add a new topic about arts so that currently user can discuss about article authors with chatbot

![alt text](https://github.com/wuhaoqiu/simple-chatbot/blob/haoqiuwu/screenshots/new%20topic.png)

*Current chatbot is able to deal with user misspelling as long as such misspelling is not too confused

![alt text](https://github.com/wuhaoqiu/simple-chatbot/blob/haoqiuwu/screenshots/misspelling.png)

*Make use of other existing language tookit including sklearn library and nltk toolkit, which helps the system to deal with misspleeing input from users by WordNetLemmatizer in nltk toolkit
[nltk and sklearn tookit](https://github.com/wuhaoqiu/simple-chatbot/blob/haoqiuwu/cosc310/mysite/mlmodels/model_chatbot.py)

*Deploy this chatbot into production by using django to build the server, using the Boostrap, BotUI(a kind of Vue.js librays) to build frontend, and using ajax technique to realize the communication between frontend and backend.[AJAX and Vue.js](https://github.com/wuhaoqiu/simple-chatbot/blob/haoqiuwu/cosc310/mysite/mlmodels/templates/mlmodels/chatbot/chatbot.html),[Django.view](https://github.com/wuhaoqiu/simple-chatbot/blob/haoqiuwu/cosc310/mysite/mlmodels/views.py)

### How to use this program:
* Fork it.
* Create virtule environment and then install all dependecies in requirements.txt
* Move into the folder where manage.py exists
* Run from command line `python manage.py runserver`
* Visit 127.0.0.1:8000/mlmodels/chatbot_page/ through your browser.
* Enjoy chatting



