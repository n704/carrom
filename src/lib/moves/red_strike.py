from .move import Move

class RedStrike(Move):

    def execute(self, carrom_board, player):
        if carrom_board.red:
            player.point += 3
            carrom_board.red -= 1
