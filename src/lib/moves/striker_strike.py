from .move import Move

class StrikerMove(Move):

    def execute(self, carrom_board, player):
        player.point -= 1
        player.foul_move += 1
        self.check_foul_move(player)
