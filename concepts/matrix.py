import numpy as np

class matrix:
    mtx1 = None
    mtx2 = None

    def __init__(self, method:str) -> None:
        self.method = method

    def __add__(self):
        return self.mtx1 + self.mtx2
    
    