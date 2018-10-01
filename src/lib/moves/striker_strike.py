from .move import Move

class StrikerMove(Move):

    def execute(self, carrom_board, player):
        player.point -= 1
