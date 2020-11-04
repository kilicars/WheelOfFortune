import random
from players.player import Player
import constants


class ComputerPlayer(Player):
    def __init__(self, name, difficulty):
        super().__init__(name)
        self.difficulty = difficulty

    def smart_coin_flip(self):
        rand_number = random.randint(1, 10)
        return rand_number > self.difficulty

    def get_possible_letters(self, guessed):
        result = []
        for letter in constants.LETTERS:
            if letter not in guessed:
                if letter in constants.VOWELS:
                    if self.prize_money >= constants.VOWEL_COST:
                        result.append(letter)
                else:
                    result.append(letter)
        return result

    def get_move(self, guessed):
        possible_letters = self.get_possible_letters(guessed)
        if len(possible_letters) == 0:
            return "pass"
        if self.smart_coin_flip():
            for letter in constants.SORTED_FREQUENCIES:
                if letter in possible_letters:
                    return letter
        else:
            return random.choice(possible_letters)
