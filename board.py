import json
import random
import constants


class Board:

    def __init__(self, file):
        self.file = file
        self.category = ""
        self.phrase = ""
        self.guessed_letters = []

    def get_phrases(self):
        with open(self.file, "r") as f:
            phrases = json.loads(f.read())
            return phrases

    # Returns a category & phrase (as a tuple) to guess
    # Example:
    #     ("Artist & Song", "Whitney Houston's I Will Always Love You")
    def get_random_category_and_phrase(self):
        phrases = self.get_phrases()
        category = random.choice(list(phrases.keys()))
        phrase = random.choice(phrases[category])
        return category, phrase.upper()

    def set_category_phrase(self):
        self.category, self.phrase = self.get_random_category_and_phrase()

    # Given a phrase and a list of guessed letters, returns an obscured version
    # Example:
    #     guessed: ['L', 'B', 'E', 'R', 'N', 'P', 'K', 'X', 'Z']
    #     phrase:  "GLACIER NATIONAL PARK"
    #     returns> "_L___ER N____N_L P_RK"
    @staticmethod
    def obscure_phrase(phrase, guessed):
        result = ""
        for s in phrase:
            if (s in constants.LETTERS) and (s not in guessed):
                result = result + "_"
            else:
                result = result + s
        return result

    # Returns a string representing the current state of the game
    def get_current_board(self):
        return f"Category: {self.category}\nPhrase:   {self.obscure_phrase(self.phrase, self.guessed_letters)}\n" \
               f"Guessed:  {', '.join(sorted(self.guessed_letters))}"

    def add_guessed_letter(self, letter):
        self.guessed_letters.append(letter)

    def is_phrase_revealed(self):
        return self.obscure_phrase(self.phrase, self.guessed_letters) == self.phrase
