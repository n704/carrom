import abc, six


@six.add_metaclass(abc.ABCMeta)
class Move(object):

    @abc.abstractmethod
    def execute(self, carrom_board, player):
        pass

    def check_foul_move(self, player):
        """
        if foul_move is greater than or equal to 3 point reduce by 1
        """
        if player.foul_move == 3:
            player.point -= 1
            player.foul_move = 0
