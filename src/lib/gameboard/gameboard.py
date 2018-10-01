from .carrom_board import CarromBoard
from .player import Player

class Game(object):
    """
    Create Game object.
    """

    def __init__(self):
        """
        Create a game board and add Player.
        """
        self.carrom_board = CarromBoard()
        self.carrom_board.player1 = Player()
        self.carrom_board.player2 = Player()

    def __str__(self):
        return str(self.carrom_board)

    def play_game(self):
        while self.carrom_board.should_play():
            self.carrom_board.update_next_player()
            self.carrom_board.next_player_make_move()
            self.carrom_board.check_board_status()
        print self.carrom_board.get_winner()
