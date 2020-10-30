
# TODO: Follow the assignment instructions to complete the required routes!
# (And make sure to delete this TODO message when you're done!)

# Import the flask library
from flask import Flask

# Set up the `app` variable to start writing routes
app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return "Are you there, world? It's me, Ducky!"

@app.route('/penguins')
def penguins():
    """Displays a message to the user about penguins, Meredith's favorite animal."""
    return "Penguins are cute!"

@app.route('/tigers')
def tigers():
    """Displays a message to the user about tigers, my favorite animal."""
    return "Tigers are cool!"

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Displays a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """Displays a message to the user that changes based on their favorite dessert."""
    return f'How did you know I liked {users_dessert}?'

@app.route('/madlibs/<adjective>/<noun>')
def mad_libs(adjective, noun):
    """Displays a (humorous) message to the user that changes based on the adjective and the noun provided by the user."""
    return f'I like to order {adjective} {noun} from Chipotle.'

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    """Checks if the user's two inputs are numbers, multiplies them, and then displays the result to the user."""
    # Check if both inputs are strings that are entirely digits
    if number1.isdigit() and number2.isdigit():
        # Cast the inputs as integers and multiply them
        result = int(number1) * int(number2)
        return f'{number1} times {number2} is {result}.'
    else:
        return "Invalid inputs. Please try again by entering 2 numbers!"

@app.route('/sayntimes/<word>/<n>')
def sayntimes(word, n):
    """Checks if the user's second input is a number and then displays the input word that number of times to the user."""
    # Check if the second input consists entirely of digits
    if n.isdigit():
        # Multiply the input word with a space at the end by the input number (string multiplication)
        repeated_word = (word + ' ') * int(n)
        # Display the repeated word and apply .strip() to remove trailing space after the last word
        return f'{repeated_word.strip()}'
    else:
        return "Invalid input. Please try again by entering a word and a number!"

if __name__ == '__main__':
    app.run(debug=True)
