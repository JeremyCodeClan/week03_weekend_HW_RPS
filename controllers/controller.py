from flask import request, redirect, render_template
from app import app
from models.game import Game
from models.player_computer import computer_1
from models.player_you import player_1

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rules')
def rules():
    return render_template('rules.html')

@app.route('/play')
def play_index():
    player_1.initialize()
    computer_1.initialize()
    return render_template('game.html')

@app.route('/play', methods=['POST'])
def play_post():
    if player_1.name == '':
        player_1.name = request.form['name']
    player_1.move = request.form['move']
    computer_1.name = 'Computer'
    computer_1.random_pick()
    game = Game(player_1, computer_1)
    result = game.play()
    if type(result) == str:
        result = 'invalid input'
    return render_template('game.html', result = result)