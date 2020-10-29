
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
    """Shows a message about penguins, Meredith's favorite animal."""
    return "Penguins are cute!"

@app.route('/tigers')
def tigers():
    """Shows a message about tigers, my favorite animal."""
    return "Tigers are cool!"




if __name__ == '__main__':
    app.run(debug=True)
