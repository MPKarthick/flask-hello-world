# import Flask class from flask package
from flask import Flask

# creating application object
app = Flask(__name__)

# use the decorator pattern to
#   link the view function to the URL
@app.route("/")
@app.route("/hello")
# define the view function, which returns the string
def hello_world():
    return "Hello World"


@app.route("/hello1")
def hello_world1():
    return "Hello World1"

# start the development server using run() method
if __name__ == '__main__':
    app.run()