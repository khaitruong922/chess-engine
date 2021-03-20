from constants.pieces import *


class Board:
    def __init__(self):
        self.data = [
            [BR, BN, BB, BQ, BK, BB, BN, BR],
            [BP, BP, BP, BP, BP, BP, BP, BP],
            [OO, OO, OO, OO, OO, OO, OO, OO],
            [OO, OO, OO, OO, OO, OO, OO, OO],
            [OO, OO, OO, OO, OO, OO, OO, OO],
            [OO, OO, OO, OO, OO, OO, OO, OO],
            [WP, WP, WP, WP, WP, WP, WP, WP],
            [WR, WN, WB, WQ, WK, WB, WN, WR],
        ]
