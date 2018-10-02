from .move import Move


class StrikeMove(Move):

    def execute(self, carrom_board, player):
        """
        """
        if (not carrom_board.red) or (carrom_board.black >= 2 and carrom_board.red):
            player.point += 1
            carrom_board.black -= 1
            player.foul_move = 0
        else:
            player.foul_move += 1
        self.check_foul_move(player)
