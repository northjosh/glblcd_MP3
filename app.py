from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin


app = Flask(__name__)

cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'


def bold(func):
    def inner():
        text = func()
        return text.lower()

    return inner
        

users = {
    "northjosh": "northjosh",
    "gabe": "gabe123",
    "charly": "charlyyy"
}


@app.get("/")
# @bold
def index():
    return render_template('login.html')


@app.route("/login", methods=['POST'])
def login():

    username = request.form['username'] 
    password = request.form['password']

    print(username, password)

    pwd = users.get(username) 
    if pwd == None:
        return(render_template('index.html', message="Username does not exist"))
    elif password != pwd:
        return(render_template('index.html', message="Incorrect Password"))
    else:
        return(render_template('home.html', name=username))


@app.get("/greet/<name>/<age>")
def greet(name, age):
    return f"<h1>Hello {name}, You are {age} years old</h1>"


@app.post("/load")
def load():

    f = request.files['file']
    f = save(secure_filename(f.file))
    



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

print(__name__)