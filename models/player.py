import random

class Player():

    def __init__(self, name = '', move = ''):
        self.name = name
        self.move = move
        self.score = 0
        self.draw = 0
        self.options = ['rock', 'paper', 'scissors']

    def initialize(self):
        self.name = ''
        self.move = ''
        self.draw = 0
        self.score = 0

    def random_pick(self):
        self.move = random.choice(self.options)

    def win_game(self):
        self.score += 1

    def draw_game(self):
        self.draw += 1