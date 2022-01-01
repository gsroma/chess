import numpy as np
from pieces import Pawn, Rook, Knight, Bishop, King, Queen


class Board(object):

    def __init__(self) -> None:
        
        super().__init__()
        self.state = np.empty(shape=(8,8))
        self.state[:,:] = np.nan
        self.wturn = True
        self.wpieces = []
        self.bpieces = []


    def startGame(self) -> None:
        for i in range(8):

            self._addPiece(Pawn('w', (i, 1)))
            self._addPiece(Pawn('b', (i, 6)))


        self._addPiece(Rook('w', (0, 0)))
        self._addPiece(Rook('w', (7, 0)))
        self._addPiece(Rook('b', (0, 7)))
        self._addPiece(Rook('b', (7, 7)))

        self._addPiece(Knight('w', (1, 0)))
        self._addPiece(Knight('w', (6, 0)))
        self._addPiece(Knight('b', (1, 7)))
        self._addPiece(Knight('b', (6, 7)))

        self._addPiece(Bishop('w', (1, 0)))
        self._addPiece(Bishop('w', (6, 0)))
        self._addPiece(Bishop('b', (1, 7)))
        self._addPiece(Bishop('b', (6, 7)))

        self._addPiece(Queen('w', (3, 0)))
        self._addPiece(Queen('b', (3, 7)))

        self._addPiece(King('w', (4, 0)))
        self._addPiece(King('b', (4, 7)))


    def loadGame(self, filepath: str) -> None:
        pass #TODO: implement when FEIN is implemented


    def move(self, start_pos: str, end_pos: str) -> dict:
        pass


    def getPos(self, type: str):
        pass

    def _isPromotion(self, end_pos: tuple) -> bool:
        pass

    def _isLegal(self, start_pos: str, end_pos: str) -> bool:
        
        ind0 = "abcdefgh".index(start_pos[0])
        ind1 = "12345678".index(start_pos[1])
        eind0 = "abcdefgh".index(end_pos[0])
        eind1 = "12345678".index(end_pos[1])
        piece = self.state[ind0][ind1]
        
        is_legal = start_pos != end_pos # Isn't same position
        is_legal = is_legal and self._checkMoveFormat(start_pos) and self._checkMoveFormat(end_pos) #Legal format
        is_legal = is_legal and piece.isLegal((ind0, ind1), (eind0, eind1)) #Piece can move that way

        if type(piece) != Knight: #No pieces in the way
            
            
            True



       
        #TODO: Finish
        return is_legal

    def _checkMoveFormat(self, move: str) -> bool:
        
        return len(move) == 2 and  move[0] in "abcdefgh" or move[1] in "12345678"

    def _addPiece(self, piece) -> None:
        
        if piece.color == 'w':
            self.wpieces.append(piece)
        else:
            self.bpieces.append(piece)

        pos = piece.position
        self.state[pos[0], pos[1]] = piece
        