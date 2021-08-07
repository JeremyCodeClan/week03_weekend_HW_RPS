from flask import request, redirect, render_template
from app import app
from models.player import Player
from models.game import Game

@app.route('/')
def index():
    return 'Hello!'