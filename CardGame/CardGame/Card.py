class Card():
    '''
    Card class that creates card with rank and suit provided in xtor. Contains static ranks and suits for outside references
    '''

    #start at 2 ends at 14. Values above 10 correspond to Jack, Queen, King, Ace
    ranks = [2,3,4,5,6,7,8,9,10,11,12,13,14] 
    #D - Diamond, C- Club, H - Heart, S - Spade
    suits = ['D','C','H','S']

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
            
    def get_real_rank(self, input):
        switcher = {
            1: str(1),
            2: str(2),
            3: str(3),
            4: str(4),
            5: str(5),
            6: str(6),
            7: str(7),
            8: str(8),
            9: str(9),
            10: str(10),
            11: "J",
            12: "K",
            13: "Q",
            14: "A"
        }
        return switcher.get(input, lambda: "Not found")
        
    def __str__(self):
        return "[" + self.get_real_rank(self.rank) + "," + self.suit + "]"
