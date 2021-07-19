from flask import Flask
from random import randint

random_number = randint(0, 9)
print(random_number)

app = Flask(__name__)


@app.route('/')
def home_route():
    return '<h1>Guess the number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route("/<int:guess>")
def guess_number(guess):
    if guess == random_number:
        return f'<h1 style="color:green">You found me<h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    elif guess > random_number:
        return f'<h1 style="color:purple">Is to high<h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    else:
        return f'<h1 style="color:red">Too low, try again<h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)
