class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    def __repr__(self):
        return f'<{self.suit}-{self.rank}>'
    

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = '黑桃 方块 梅花 红桃'.split()
    
    def __init__(self):
        self._cards = [
			Card(rank, suit) for suit in self.suits for rank in self.ranks
		]
        
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
    
if __name__ == '__main__':
    beer_card = Card('7', '方块')
    print(beer_card.rank, beer_card.rank)
    
    deck = FrenchDeck()
    print(len(deck))
    print(deck[0].suit, deck[0].rank)
    print(deck[0:-1])
    
    from random import choice
    
    print(choice(deck))