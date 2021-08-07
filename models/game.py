from models.player import Player

class Game():

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        # self.result = {1: 'win', 2: 'lose', 3: 'draw'}

    def play(self):
        if self.player_1.move == self.player_2.move:
            return None
        elif self.player_1.move == 'rock' and self.player_2.move == 'paper':
            return self.player_2
        elif self.player_1.move == 'paper' and self.player_2.move == 'scissors':
            return self.player_2
        elif self.player_1.move == 'scissors' and self.player_2.move == 'rock':
            return self.player_2
        else:
            return self.player_1
    # rock, paper, scissors