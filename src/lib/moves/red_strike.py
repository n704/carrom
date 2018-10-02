from .move import Move

class RedStrike(Move):

    def execute(self, carrom_board, player):
        if carrom_board.red and carrom_board.black >= 1:
            player.point += 3
            carrom_board.red -= 1
        else:
            player.foul_move += 1
        self.check_foul_move(player)
