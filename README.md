To create a rock, paper, scissors game using Python and HTML, we will need to use a web framework that allows us to write Python code for the backend and HTML for the frontend. Flask is a good choice for this. 

Here are the core classes, functions, methods that will be necessary:

1. `app.py`: This is the main entry point of our application. It will contain the Flask application and the routes for our game.

2. `game.py`: This file will contain the logic for the rock, paper, scissors game. It will have a `Game` class with methods like `play_round`, `get_computer_choice`, and `determine_winner`.

3. `templates/index.html`: This is the HTML file that will display the game interface to the user. It will have buttons for the user to choose rock, paper, or scissors, and it will display the result of each round.

4. `static/style.css`: This is the CSS file that will style our HTML page.

5. `requirements.txt`: This file will list all the Python dependencies that our application needs to run.

Let's start with the `app.py` file:

app.py
