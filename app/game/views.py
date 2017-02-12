#need to review these imports to confirm whta is actually needed
from flask import render_template, session, redirect, request, url_for, current_app, flash, jsonify
from .. import db
from ..models import User
from . import game
from .forms import GameForm
#game logic related imports
from random import randint
from collections import deque

#need to figure out how to render a different version of the specific game's page for each player

#below is flask jQuery attempt at game page

@game.route('/gamepage', methods=['GET', 'POST'])
def game_view():
    form = GameForm()
    return render_template('game/game.html', form=form)