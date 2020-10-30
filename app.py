
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
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """Display a message to the user that changes based on their favorite dessert."""
    return f'How did you know I liked {users_dessert}?'

if __name__ == '__main__':
    app.run(debug=True)
