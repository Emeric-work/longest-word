import string
import random

class Game:
    def __init__(self : str) -> list:
        self.grid=[random.choice(string.ascii_uppercase) for i in range(9)]

    #def is_valid(self,word:str) -> bool:
     #   all(i in self for i in word)

    def is_valid(self, word):
        if not word:
            return False
        letters = self.grid.copy() # Consume letters from the grid
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        return True
