from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "welcome to my website"

@app.route("/home")
def home():
    return "welcome to my homepage"

@app.route("/contacts")
def cont():
    return "welcome to my contactsname"


if(__name__=="__main__"):
    app.run()