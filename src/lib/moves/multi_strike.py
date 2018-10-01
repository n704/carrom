from .move import Move

class MultiStrike(Move):

    def execute(self, carrom_board, player):
        player.point += 2
