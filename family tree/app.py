# importing modules from flask library
from flask import Flask , render_template, render_template_string

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "raju" # write your name
    age = "15" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")   
def father():

    name = "ram " # write your father name
    age = "34" # write your father's age

    return render_template('father.html', name = name, age = age)

# define the route to mother webpage
@app.route("/mother")
def mother():

    name = "lakshmi" # write your mother's name
    age = "33" # write your mother's age

    return render_template('mother.html', name = name, age = age)


# define the route to friends webpage
@app.route("/friend")
def friend():

    name = "shyam" # write your friend's name
    age = "15" # write your friends's age

    return render_template('friend.html', name = name, age = age)

# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
