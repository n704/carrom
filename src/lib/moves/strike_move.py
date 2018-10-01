from .move import Move

class StrikeMove(Move):

    def execute(self, carrom_board, player):
        """
        """
        player.point += 1
        carrom_board.black -= 1
