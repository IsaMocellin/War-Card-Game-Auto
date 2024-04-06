class Card:
    def __init__(self, suit, rank, values):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]  # Atribui o valor com base no rank definido no dicionário values
        
    def __str__(self):
        return f"{self.rank} of {self.suit}"
