import random

class Game:
    CHOICES = ['rock', 'paper', 'scissors']

    def get_computer_choice(self):
        return random.choice(self.CHOICES)

    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return 'It\'s a tie!'
        if (player_choice == 'rock' and computer_choice == 'scissors') or \
           (player_choice == 'paper' and computer_choice == 'rock') or \
           (player_choice == 'scissors' and computer_choice == 'paper'):
            return 'You win!'
        return 'You lose!'
