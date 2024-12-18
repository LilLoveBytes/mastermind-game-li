from flask import Blueprint 
from app.models import gameController

game_bp = Blueprint('game', __name__)

@game_bp.route('/start', methods=['POST'])
def start_game():
    return gameController.start_game()

@game_bp.route('/guess', methods=['POST'])
def submit_guess():
    return gameController.submit_guess()
    