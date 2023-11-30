from flask import Flask, render_template, request
from game import Game

app = Flask(__name__)
game = Game()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        player_choice = request.form.get('choice')
        computer_choice = game.get_computer_choice()
        result = game.determine_winner(player_choice, computer_choice)
        return render_template('index.html', player_choice=player_choice, computer_choice=computer_choice, result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
