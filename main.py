from flask import Flask

app = Flask(__name__)

from route import *
    

if __name__ == "__main__":
    app.run()