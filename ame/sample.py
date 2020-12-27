from flask import Flask,render_template,request
from flask_ngrok import run_with_ngrok

#render is for giving context to html file
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
 

app=Flask(__name__) #we are creating an application that contains an application called app
run_with_ngrok(app) #start ngrok when app is run
english_bot= ChatBot("Chatterbot",storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer=ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")
trainer.train("data/data.yml")
trainer.train("data/depression.yml")


@app.route("/") #we are routing as we are creating an api with flask
#this dummy url will have a slash towards the end

def index():
    return render_template("index.html")#to send context to html file

@app.route("/get") #to get the bot's response
def get_bot_response():
    userText=request.args.get("msg") #get data from input where we write our js
    return str(english_bot.get_response(userText))

if __name__ == "__main__":
    app.run()