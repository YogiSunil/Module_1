
from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return "Are you there, world? It's me, Ducky!"

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """Display a message about the user's favorite dessert."""
    return f'How did you know I liked {users_dessert}?'

@app.route('/madlibs/<adjective>/<noun>')
def mad_libs(adjective, noun):
    """Display a funny story using the provided adjective and noun."""
    return f'Today was a {adjective} day because I found a {noun}!'

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    """Multiply two numbers and return the result."""
    if number1.isdigit() and number2.isdigit():
        result = int(number1) * int(number2)
        return f'{number1} times {number2} is {result}.'
    else:
        return 'Invalid inputs. Please try again by entering 2 numbers!'

@app.route('/sayntimes/<word>/<n>')
def say_n_times(word, n):
    """Repeat a string a given number of times."""
    if n.isdigit():
        n = int(n)
        return ' '.join([word] * n)
    else:
        return 'Invalid input. Please try again by entering a word and a number!'

@app.route('/dicegame')
def dice_game():
    """Simulate a dice game where the user rolls a dice."""
    roll = random.randint(1, 6)
    if roll == 6:
        return f'You rolled a {roll}. You won!'
    else:
        return f'You rolled a {roll}. You lost!'

if __name__ == '__main__':
    app.run(debug=True)

