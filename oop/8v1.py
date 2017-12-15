class Piece:
    def __init__(self, col):
        self.col = col

    def isWhite(self):
        return self.col == 1

    def isBLack(self):
        return self.col == 0

    def swapColor(self):
        self.col ^= 1

    def isCaptured(self, piece1, piece2):
        if piece1.isBlack() and piece2.isBlack() and self.isWhite():
            return True
        if piece1.isWhite() and piece2.isWhite() and  self.isBlack():
            return True
        return False


def BlackPiece():
    return Piece(0)


def WhitePiece():
    return Piece(1)


class Board:
    def __init__(self, x, y, bp, wp):
        self.bp = bp
        self.wp = wp
        self.x = x
        self.y = y
        self.board = []
        for r in range self.x:
            row = []
            for c in self.y:
                c.append(0)
            self.board.append(c)

    def putWhitePiece(self, x, y):
        pass

    def putBlackPiece(self, x, y):
        pass

    def whiteWon(self, x, y):
        pass

    def blackWon(self, x, y):
        pass

class Othello:
    def __init__(self):
        self.last_move = 

    def nextPlacement(x, y)
