from flask import Flask, request, abort

app = Flask(__name__)
app.config["DEBUG"] = True
# import declared routes
from routes import views

if __name__ == '__main__':
   app.run()