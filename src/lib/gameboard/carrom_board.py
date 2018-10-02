class CarromBoard(object):
    """
    Create Carrom Board and its pieces.
    """
    def __init__(self):
        """
        Board has 9 black 1 red and 1 striker.
        """
        self.black = 9
        self.red = 1
        self.striker = 1
        self.player1 = None
        self.player2 = None
        self.next_player = None

    def __str__(self):
        return "black:{0}, red:{1}, [player1: {2}], [player2: {3}]".format(
            self.black, self.red, str(self.player1), str(self.player2)
        )

    def get_next_player(self):
        """
        Return who plays next game.
        """
        player = None
        if self.next_player:
            player = self.next_player
        if player == self.player1:
            return self.player2
        return self.player1

    def should_play(self):
        """
        tell the game should it continue playingself.

        @returns bool status
        """
        if self.black:
            return True
        return False

    def update_next_player(self):
        self.next_player = self.get_next_player()
        print self.next_player

    def get_player_num(self):
        if self.next_player == self.player2:
            return "2"
        return "1"

    def print_moves(self):
        print'''
Player {0}: Choose an outcome from the list below
1. Strike
2. Multistrike
3. Red strike
4. Striker strike
5. Defunct coin
6. None'''.format(self.get_player_num())

    def next_player_make_move(self):
        from .player import Player
        self.print_moves()
        self.next_player.make_move(self)
        # self.player1.status = Player.WINNER

    def check_board_status(self):
        """
        """
        self.next_player.update_status()


    def get_winner(self):
        """
        Return Winner status and final score of the game
        """
        player1_points = self.player1.get_score()
        player2_points = self.player2.get_score()
        player_scored_less_than_5 = (player1_points < 5 and player2_points < 5)
        player_lead_less_than_3 = (abs(player1_points - player2_points) < 3)
        if player_scored_less_than_5 or player_lead_less_than_3:
            return "Game is Draw"
        if self.player1.is_winner():
            return "Player 1 won the game. Final Score: {0}-{1}".format(
                self.player1.get_score(), self.player2.get_score()
            )
        return "Player 2 won the game. Final Score: {0}-{1}".format(
            self.player2.get_score(), self.player1.get_score()
        )
