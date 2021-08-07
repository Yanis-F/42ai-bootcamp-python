

import builtins


class GotCharacter:
    def __init__(self, first_name: str, is_alive: bool = True):
        self.first_name = first_name
        self.is_alive = True

    def die(self):
        self.is_alive = False

class Stark(GotCharacter):
    def __init__(self, first_name: str, is_alive: bool = True):
        super().__init__(first_name, is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"
        
    def print_house_words(self):
        print(self.house_words)