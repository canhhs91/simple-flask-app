from db import db
from flask import request

from .models import Card, Deck
from .schemas import MoveCardRequestData


def all():
    return {'message': 'Not implemented'}, 501


def getDeck(deck_id):
    return {'message': 'Not implemented'}, 501


def getCard(card_id):
    return {'message': 'Not implemented'}, 501


def moveCard(card_id):
    payload = MoveCardRequestData(**request.json)
    card = db.session.get(Card, card_id)
    if card is None:
        return {'message': 'Card not found'}, 404
    deck = db.session.get(Deck, payload.deck_id)
    if deck is None:
        return {'message': 'Deck not found'}, 404
    if payload.position < 0 or payload.position > len(deck.cards):
        return {'message': 'Invalid position'}, 400
    if payload.deck_id == card.parent_id:
        # move card inside the same deck

        if payload.position > card.position:
            # move card up
            cards_to_update = deck.cards.filter(Card.position > card.position, Card.position <= payload.position)
            decks_to_update = deck.decks.filter(Deck.position > card.position, Deck.position <= payload.position)
            cards_to_update.update({Card.position: Card.position - 1})
            decks_to_update.update({Deck.position: Deck.position - 1})
        else:
            # move card down
            cards_to_update = deck.cards.filter(Card.position < card.position, Card.position >= payload.position)
            decks_to_update = deck.decks.filter(Deck.position < card.position, Deck.position >= payload.position)
            cards_to_update.update({Card.position: Card.position + 1})
            decks_to_update.update({Deck.position: Deck.position + 1})
        card.position = payload.position
    else:
        # move card to another deck

        # update new deck
        cards_to_update = deck.cards.filter(Card.position >= payload.position)
        decks_to_update = deck.decks.filter(Deck.position >= payload.position)
        cards_to_update.update({Card.position: Card.position + 1})
        decks_to_update.update({Deck.position: Deck.position + 1})

        # update old deck
        old_parent_deck = db.session.get(Deck, card.parent_id)
        cards_to_update = old_parent_deck.cards.filter(Card.position > card.position)
        decks_to_update = old_parent_deck.decks.filter(Deck.position > card.position)
        cards_to_update.update({Card.position: Card.position - 1})
        decks_to_update.update({Deck.position: Deck.position - 1})

        card.parent_id = payload.deck_id
        card.position = payload.position

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return {'message': str(e)}, 500
    return {'message': 'Card moved'}, 200


def moveDeck(deck_id):
    payload = MoveCardRequestData(**request.json)
    deck = db.session.get(Deck, deck_id)
    if deck is None:
        return {'message': 'Deck not found'}, 404
    parent_deck = db.session.get(Deck, deck.parent_id)
    new_parent_deck = db.session.get(Deck, payload.deck_id)
    if parent_deck is None:
        return {'message': 'Parent deck not found'}, 404
    if payload.position < 0 or payload.position > len(parent_deck.decks):
        return {'message': 'Invalid position'}, 400

    if payload.deck_id == parent_deck.parent_id:
        # move card inside the same deck

        if payload.position > parent_deck.position:
            # move deck up
            cards_to_update = parent_deck.cards.filter(Card.position > deck.position, Card.position <= payload.position)
            decks_to_update = parent_deck.decks.filter(Deck.position > deck.position, Deck.position <= payload.position)
            cards_to_update.update({Card.position: Card.position - 1})
            decks_to_update.update({Deck.position: Deck.position - 1})
        else:
            # move deck down
            cards_to_update = parent_deck.cards.filter(Card.position < deck.position, Card.position >= payload.position)
            decks_to_update = parent_deck.decks.filter(Deck.position < deck.position, Deck.position >= payload.position)
            cards_to_update.update({Card.position: Card.position + 1})
            decks_to_update.update({Deck.position: Deck.position + 1})
        deck.position = payload.position
    else:
        # move deck to another deck

        # update new deck
        cards_to_update = new_parent_deck.cards.filter(Card.position >= payload.position)
        decks_to_update = new_parent_deck.decks.filter(Deck.position >= payload.position)
        cards_to_update.update({Card.position: Card.position + 1})
        decks_to_update.update({Deck.position: Deck.position + 1})

        # update old deck
        parent_deck = db.session.get(Deck, deck.parent_id)
        cards_to_update = parent_deck.cards.filter(Card.position > deck.position)
        decks_to_update = parent_deck.decks.filter(Deck.position > deck.position)
        cards_to_update.update({Card.position: Card.position - 1})
        decks_to_update.update({Deck.position: Deck.position - 1})

        deck.parent_id = payload.deck_id
        deck.position = payload.position

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return {'message': str(e)}, 500
    return {'message': 'Card moved'}, 200
