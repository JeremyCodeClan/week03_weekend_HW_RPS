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
    return 'play!'
    