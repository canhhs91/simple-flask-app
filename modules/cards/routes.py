from flask import Blueprint
from .controllers import all, getDeck, getCard, moveCard, moveDeck

blueprint = Blueprint('cards', __name__)

# get all level 0 decks and cards
blueprint.route('/', methods=['GET'])(all)

# get deck info & all cards & decks in a deck
blueprint.route('/<int:deck_id>', methods=['GET'])(getDeck)

# get card info
blueprint.route('/<int:card_id>', methods=['GET'])(getCard)

# move card to another deck
blueprint.route('/card/<int:card_id>/move', methods=['POST'])(moveCard)

# move deck to another deck
blueprint.route('/deck/<int:deck_id>/move', methods=['POST'])(moveDeck)
