from typing import Iterator
import numpy as np
import itertools

from pieces import Pawn, Rook, Knight, Bishop, King, Queen

EMPTY_INDICATOR = 0


class Board(object):

    def __init__(self) -> None:
        
        super().__init__()
        self.state = np.empty(shape=(8,8))
        self.state[:,:] = EMPTY_INDICATOR
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

        self._addPiece(Bishop('w', (2, 0)))
        self._addPiece(Bishop('w', (5, 0)))
        self._addPiece(Bishop('b', (2, 7)))
        self._addPiece(Bishop('b', (5, 7)))

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
        piece = self.state[ind0, ind1]
        
        is_legal = start_pos != end_pos # Isn't same position
        is_legal = is_legal and self._checkMoveFormat(start_pos) and self._checkMoveFormat(end_pos) #Legal format
        is_legal = is_legal and piece.isLegal((ind0, ind1), (eind0, eind1)) #Piece can move that way
  
        if eind0 == ind0: # Vertical moves
            for index in range(min(ind1, eind1) + 1, max(ind1, eind1)):
                islegal = islegal and self.state[ind0, index] == EMPTY_INDICATOR

        elif eind1 == ind1: # Horizontal moves
            for index in range(min(ind0, eind0) + 1, max(ind0, eind0)):
                islegal = islegal and self.state[index, ind1] == EMPTY_INDICATOR

        elif np.abs(eind1 - ind1) == np.abs(eind0 - ind0): # Diagonal moves
            h_range = range(ind0, eind0) if ind0 < eind0 else reversed(range(ind0, eind0))
            v_range = range(ind1, eind1) if ind1 < eind1 else reversed(range(ind1, eind1))

            for i in zip(h_range, v_range):
                islegal = islegal and self.state[i] == EMPTY_INDICATOR

        # Is not moving into check
        color = piece.color

        new_board = self.state.copy()
        new_board[ind0, ind1] = EMPTY_INDICATOR
        new_board[eind0, eind1] = piece

        islegal = islegal and not self._isCheck(color, new_board)

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

    @classmethod
    def _isCheck(self, color: str, board: np.ndarray) -> bool:

        for ind0 in range(8): # Get king
            for ind1 in range(8):
                curr_piece = board[ind0, ind1]

                if type(curr_piece) == King and curr_piece.color == color:
                    break
        
        for index in reversed(range(0, ind0)): # Check left
            piece = board[index, ind1]

            if piece != EMPTY_INDICATOR:
                if piece.color == color:
                    break

                elif type(piece) in (Rook, Queen):
                    return True

        for index in range(ind0 + 1, 8): # Check right
            piece = board[index, ind1]

            if piece != EMPTY_INDICATOR:
                if piece.color == color:
                    break

                elif type(piece) in (Rook, Queen):
                    return True

        for index in reversed(range(0, ind1)): # Check down
            piece = board[ind0, index]

            if piece != EMPTY_INDICATOR:
                if piece.color == color:
                    break

                elif type(piece) in (Rook, Queen):
                    return True
 
        for index in range(ind1 + 1, 8): # Check up
            piece = board[ind0, index]

            if piece != EMPTY_INDICATOR:
                if piece.color == color:
                    break

                elif type(piece) in (Rook, Queen):
                    return True


        for iterator in range(1, min(8 - ind0, 8 - ind1)): # Diagonal (1, 1)
            piece = board[ind0 + iterator, ind1 + iterator]
            
            if piece != EMPTY_INDICATOR:
                if piece.color == color:
                    break
            elif type(piece) in (Bishop, Queen) or (type(piece) == Pawn and iterator == 1):
                return True

        for iterator in range(1, min(ind0, ind1)): # Diagonal (-1, -1)
            piece = board[ind0 - iterator, ind1 - iterator]
            
            if piece != EMPTY_INDICATOR:
                if piece.color == color:
                    break
            elif type(piece) in (Bishop, Queen) or (type(piece) == Pawn and iterator == 1):
                return True                
                       
        for iterator in range(1, min(8 - ind0, ind1)): # Diagonal (1, -1)
            piece = board[ind0 + iterator, ind1 - iterator]
            
            if piece != EMPTY_INDICATOR:
                if piece.color == color:
                    break
            elif type(piece) in (Bishop, Queen) or (type(piece) == Pawn and iterator == 1):
                return True

        for iterator in range(1, min(ind0, 8 - ind1)): # Diagonal (-1, 1)
            piece = board[ind0 - iterator, ind1 + iterator]
            
            if piece != EMPTY_INDICATOR:
                if piece.color == color:
                    break
            elif type(piece) in (Bishop, Queen) or (type(piece) == Pawn and iterator == 1):
                return True
        
        
        positions = np.array([ind0, ind1])
        k_deltas = np.array([[-2, -1],
                            [-2, 1],
                            [-1, -2],
                            [-1, 2],
                            [1, -2],
                            [1, 2],
                            [2, -1],
                            [2, 1]])
                            
        positions = positions + k_deltas
        mask = np.logical_and(0 <= positions, 7 >= positions)
        mask = mask.all(axis = 1)
        positions = positions[mask].reshape((-1, 2))

        for position in positions:
            piece = board[position]
            if type(piece) == Knight and piece.color != color:
                return True

        return False
        

    def _allLegalMoves(self, color: str, board: np.ndarray) -> list:
        
        pieces = self.wpieces if color == 'w' else self.bpieces

        for piece in pieces:
                pass
