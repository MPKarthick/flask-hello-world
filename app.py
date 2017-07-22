# import Flask class from flask package
from flask import Flask

# creating application object
app = Flask(__name__)

# adding debug mode so no need to restart the server
# everytime we do changes in code
app.config['DEBUG'] = True

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

# dynamic route where tha URL is converted as string
@app.route("/<search_query>")
def search(search_query):
    return search_query

# dynamic route where u want to pass or convert to string
# this is done by using convertors
# int --> integer
# float --> accepts decimal value
# path --> same as string accepts slashes
# any --> matches 1 of the item provided
# uuid --> accepts UUID string
@app.route("/<int:post_id>")
def search_number(post_id):
    return "post id: %d"%post_id

#dynamic route that accepts	slashes
@app.route("/path/<path:value>")
def	path_type(value):
	print(value)
	return	"correct"

@app.route("/name/<name>")
def retName(name):
    if name.lower() == 'mpk':
        return "Hello, {}".format(name), 200
    else:
        return "Name not found", 404


# start the development server using run() method
if __name__ == '__main__':
    app.run()