import random
from Card import Card

class Deck():
    ''' 
    Deck class that creates a basic 52-card deck when called.
    '''

    def __init__(self):
        self.cards = []
        for suit in Card.suits:
            for rank in Card.ranks:
                self.cards.append(Card(rank, suit))
        print("Deck created!")
                        
    #returns a random card from the current deck
    def draw_card(self):
        return self.cards.pop(random.randint(0, len(self.cards)))
        
    #prints remaining cards
    def current_deck(self):
        for card in self.cards:
            print(card)
