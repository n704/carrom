from .strike_move import StrikeMove
from .multi_strike import MultiStrike
from .red_strike import RedStrike
from .striker_strike import StrikerMove
from .defunt_move import DefunMove

def getMove(move):
    if move == 1:
        return StrikeMove()
    elif move == 2:
        return Multistrike()
    elif move == 3:
        return RedStrike()
    elif move == 4:
        return StrikerMove()
    elif move == 5:
        return DefunMove()
    return StrikeMove()
