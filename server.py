import random
from flask import Flask

app = Flask(__name__)
random_number = random.randint(0,9)

@app.route('/')
def hello():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>" \
           f"{random_number}"

@app.route('/<n>')
def show(n):
    n = int(n)
    if n == random_number:
        return "Right" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
    elif n < random_number:
        return "Too low" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    else:
        return "Too high" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"

if __name__=="__main__":
    app.run(debug=True)