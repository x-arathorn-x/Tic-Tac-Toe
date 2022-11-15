import math

class Player():
    def __init__(self, identity):
        self.identity = identity
    def get_move(self, game):
        pass


class HumanPlayer(Player):
    def __init__(self, identity):
        super().__init__(identity)
        
    def get_move(self, game):
        legal_square = False
