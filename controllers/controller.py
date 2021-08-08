from flask import request, redirect, render_template
from app import app
from models.player import Player
from models.game import Game

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rules')
def rules():
    return 'rules!'

@app.route('/<player1>/<player2>')
def play_game(player1, player2):
    player_1 = Player('Player 1', player1.lower())
    player_2 = Player('Player 2', player2.lower())
    game = Game(player_1, player_2)
    result = game.play()
    if type(result) == str:
        result = 'invalid input'
    return render_template('game.html', result = result)
    
# rock, paper, scissors