# Import the flask library
from flask import Flask
# Import the random library for the Dice Game challenge
import random

# Set up the `app` variable to start writing routes
app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return "Are you there, world? It's me, Ducky!"

@app.route('/penguins')
def penguins():
    """Displays a message to the user about penguins, Meredith's favorite animal."""
    return 'Penguins are cute!'

@app.route('/tigers')
def tigers():
    """Displays a message to the user about tigers, my favorite animal."""
    return 'Tigers are cool!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Displays a message to the user that changes based on their favorite animal."""
    return f'Wow, the {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """Displays a message to the user that changes based on their favorite dessert."""
    return f'How did you know that I liked {users_dessert}?'

@app.route('/madlibs/<adjective>/<noun>')
def mad_libs(adjective, noun):
    """Displays a (humorous) message to the user that changes based on the adjective and the noun provided by the user."""
    return f'I like to order the {adjective} {noun} from Chipotle.'

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    """Checks if the user's two inputs are numbers, multiplies them, and then displays the result to the user."""
    # Check if both inputs are strings that are entirely digits
    if number1.isdigit() and number2.isdigit():
        # Cast the inputs as integers and multiply them
        result = int(number1) * int(number2)
        return f'{number1} times {number2} is {result}.'
    else:
        return 'Invalid inputs. Please try again by entering 2 numbers!'

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
        return 'Invalid input. Please try again by entering a word and a number!'

@app.route('/reverse/<word>')
def reverse(word):
    """Takes an input word from the user and displays the word in reverse for the user"""
    # Assign variable for word length
    word_len = len(word)
    # Define an empty string 
    reverse_word = ''
    # Iterate from the end of the word to the beginning and add each letter to the new string
    for i in range(word_len):
        reverse_word += word[word_len - i - 1]
    return reverse_word

@app.route('/strangecaps/<word>')
def strangecaps(word):
    """Takes an input word from the user and displays the word with letters in alternating upper and lower case for the user"""
    # Assign variable for word length
    word_len = len(word)
    # Define an empty string
    new_word = ''
    # Iterate through each letter of the word and add the modified letter to the new string
    for i in range(word_len):
        # If the index of the letter is odd, then change the letter to upper case
        if i % 2 != 0:
            new_word += word[i].upper()
        # If the index of the letter is even, then change the letter to lower case
        else:
            new_word += word[i].lower()
    return new_word
    
@app.route('/dicegame')
def dicegame():
    """Simulates a die toss by printing a message to the user with a random integer between 1 and 6 (only 6 is a win)""" 
    # Set player status to lost as default
    player_status = 'lost'
    # Randomly choose an integer between 1 and 6 (inclusive)
    die_roll = random.randint(1, 6)
    # Change player status to won only if the roll is a 6
    if die_roll == 6:
        player_status = 'won'
    return f'You rolled a {die_roll}. You {player_status}!'


if __name__ == '__main__':
    app.run(debug=True)
