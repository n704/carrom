import abc, six


@six.add_metaclass(abc.ABCMeta)
class Move(object):

    @abc.abstractmethod
    def execute(self, carrom_board, player):
        pass
