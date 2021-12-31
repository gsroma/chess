import numpy as np
#from pieces import pieces


class Board(object):
    def __init__(self) -> None:
        super().__init__()
        self.state = np.empty(shape=(8,8))
        self.wturn = True

    def startGame(self) -> None:
        pass

    def loadGame(self, filepath: str) -> None:
        pass

    def move(self, start_pos: tuple, end_pos: tuple) -> tuple:
        pass

    def _isLegal(self, start_pos: tuple, end_pos: tuple) -> bool:
        pass

    def getPos(self, type: str):
        pass

    def _isPromotion(self, end_pos: tuple) -> bool:
        pass
