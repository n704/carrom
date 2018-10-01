class Player(object):
    """
    Player objects.
    """
    PLAYING = 0
    WINNER = 1
    LOSER = 2
    def __init__(self):
        """
        A player has points and status and action.
        """
        self.action = None
        self.status = Player.PLAYING
        self.point = 0
        self.foul_move = 0

    def __str__(self):
        """String Representation."""
        return "status:{0}, point: {1}".format(self.status, self.point)

    def is_playing(self):
        """is Player is playing or won or lost."""
        return self.status == Player.PLAYING

    def make_move(self, carrom_board):
        """
        """
        try:
            move = int(raw_input())
        except TypeError:
            pass
        self.play_move(move, carrom_board)

    def update_status(self):
        if self.point >= 15:
            self.status = Player.WINNER

    def play_move(self, move, carrom_board):
        from ..moves import getMove
        strikeMove = getMove(move)
        strikeMove.execute(carrom_board, self)

    def get_score(self):
        return self.point

    def is_winner(self):
        return self.status == Player.WINNER
