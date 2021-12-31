import numpy as np


class Piece(object):
    def __init__(self, color: str) -> None:
        super().__init__()
        assert color in ('w', 'b'), "Piece color must be 'b' or 'w'."
        self.color = color
        self.repr = ''
    
    def isLegal(self, start_pos:tuple, end_pos:tuple) -> bool:
        return True

    def __str__(self) -> str:
        return self.repr

    def __repr__(self) -> str:
        return self.repr


class Pawn(Piece):
    def __init__(self, color: str) -> None:
        super().__init__(color)
        self.repr = self.color + 'P'

    def isLegal(self, start_pos: tuple, end_pos: tuple) -> bool:
        if (end_pos[1] - start_pos[1]) == 1 and self.color == 'w':
            return True
        elif (end_pos[1] - start_pos[1]) == -1 and self.color == 'b':
            return True
        
        return False


class Knight(Piece):
    def __init__(self, color: str) -> None:
        super().__init__(color)
        self.repr = self.color + 'C'

    def isLegal(self, start_pos: tuple, end_pos: tuple) -> bool:
        dx = np.abs(end_pos[0] - start_pos[0])
        dy = np.abs(end_pos[1] - start_pos[1])
        if (dx + dy == 3) and (dx == 1 or dy == 1):
            return True
        return False


class Bishop(Piece):
    def __init__(self, color: str) -> None:
        super().__init__(color)
        self.repr = self.color + 'B'

    def isLegal(self, start_pos: tuple, end_pos: tuple) -> bool:
        dx = np.abs(end_pos[0] - start_pos[0])
        dy = np.abs(end_pos[1] - start_pos[1])
        return dx == dy and dx > 0


class Rook(Piece):
    def __init__(self, color: str) -> None:
        super().__init__(color)
        self.repr = self.color + 'R'

    def isLegal(self, start_pos: tuple, end_pos: tuple) -> bool:
        dx = np.abs(end_pos[0] - start_pos[0])
        dy = np.abs(end_pos[1] - start_pos[1])
        if (dx > 0 and dy == 0 ) or (dx == 0 and dy > 0):
            return True
        return False


class Queen(Piece):
    def __init__(self, color: str) -> None:
        super().__init__(color)
        self.repr = self.color + 'Q'

    def isLegal(self, start_pos: tuple, end_pos: tuple) -> bool:
        dx = np.abs(end_pos[0] - start_pos[0])
        dy = np.abs(end_pos[1] - start_pos[1])
        if ((dx > 0 and dy == 0 ) or (dx == 0 and dy > 0)) or dx == dy:
            return True
        return False


class King(Piece):
    def __init__(self, color: str) -> None:
        super().__init__(color)
        self.repr = self.color + 'Q'

    def isLegal(self, start_pos: tuple, end_pos: tuple) -> bool:
        dx = np.abs(end_pos[0] - start_pos[0])
        dy = np.abs(end_pos[1] - start_pos[1])
        if dx <= 1 and dy <= 1 and (dx + dy) > 0:
            return True
        return False
