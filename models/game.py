from models.player import Player

class Game():

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    def check_valid(self, player):
        if player.move in player.options: return True

    # rock, paper, scissors
    def play(self):
        if self.check_valid(self.player_1) and self.check_valid(self.player_2):
            if self.player_1.move == self.player_2.move:
                self.player_1.draw_game()
                return { 'draw': True, 'player': self.player_1, 'computer': self.player_2 }
            elif ((self.player_1.move == 'rock' and self.player_2.move == 'paper') or
                (self.player_1.move == 'paper' and self.player_2.move == 'scissors') or
                (self.player_1.move == 'scissors' and self.player_2.move == 'rock')):
                self.player_2.win_game()
                return { 'player': self.player_1, 'computer': self.player_2, 'winner': self.player_2, 'loser': self.player_1 } 
            else:
                self.player_1.win_game()
                return { 'player': self.player_1, 'computer': self.player_2, 'winner': self.player_1, 'loser': self.player_2 }
        else:
            return "Invalid move input, must be 'rock', 'paper', 'scissors'"