from .move import Move

class DefunMove(Move):

    def execute(self, carrom_board, player):
        if carrom_board.black >= 1:
            player.point -= 2
        else:
            player.foul_move += 1
        self.check_foul_move(player)
