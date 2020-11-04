from players.player import Player


class HumanPlayer(Player):

    @staticmethod
    def get_move(guessed):
        prompt = "\nGuess a letter, phrase, or type 'exit' or 'pass': "
        user_input = input(prompt)
        return user_input
