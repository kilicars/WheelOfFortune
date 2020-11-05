import time
import constants
from players.computer_player import ComputerPlayer
from players.human_player import HumanPlayer
from wheel import Wheel, SpinResultType
from board import Board
from colorful import Colorful


class WheelOfFortune:

    def __init__(self, wheel_file, phrases_file):
        self.game_name = "WHEEL OF FORTUNE"
        self.wheel = Wheel(wheel_file)
        self.board = Board(phrases_file)
        self.players = None
        self.winner = None
        self.cur_player = None
        self.cur_player_index = -1
        self.colorful = Colorful()

    def print_header(self):
        symbols = "=" * 70
        header = f"{symbols}\n"
        header += f"{' ' * 27}{self.game_name}{' ' * 27}\n"
        header += f"{symbols}\n\n"
        print(self.colorful.color_text("magenta", header))

    def print_board(self):
        symbols = "-" * 70
        text = f"\n{symbols}\n{self.board.get_current_board()}\n{symbols}\n"
        print(self.colorful.color_text("blue", text))

    def init_game(self):
        self.print_header()
        self.players = self.get_players()
        if len(self.players) == 0:
            print(self.colorful.color_text("red", "We need players to play!"))
            exit()
        self.board.set_category_phrase()

    @staticmethod
    def get_human_players():
        num_human = get_number_between("How many human players? ", 0, 10)
        human_players = [HumanPlayer(input(f"Enter the name for human player #{i + 1} ")) for i in range(num_human)]
        return human_players

    @staticmethod
    def get_computer_players():
        num_computer = get_number_between("How many computer players? ", 0, 10)
        if num_computer >= 1:
            difficulty = get_number_between("What difficulty for the computers? (1-10) ", 1, 10)
            computer_players = [ComputerPlayer(f"Computer {i + 1}", difficulty) for i in range(num_computer)]
            return computer_players

    def get_players(self):
        players = []
        human_players = self.get_human_players()
        if human_players:
            players += human_players
        computer_players = self.get_computer_players()
        if computer_players:
            players += computer_players
        return players

    def set_cur_player(self):
        # Move on to the next player (or go back to player[0] if we reached the end)
        self.cur_player_index = (self.cur_player_index + 1) % len(self.players)
        self.cur_player = self.players[self.cur_player_index]

    def spin_wheel(self):
        print(self.colorful.color_text("green", f"{self.cur_player.name} spins..."))
        spin_result = self.wheel.spin()
        time.sleep(2)
        print(f"Spin outcome is {self.colorful.color_text('magenta', spin_result.text)}!")
        return spin_result

    def request_move(self, player):
        while True:  # we're going to keep asking the player for a move until they give a valid one
            time.sleep(0.1)  # added so that any feedback is printed out before the next prompt
            move = player.get_move(self.board.guessed_letters).upper()
            if len(move) == 1:  # they guessed a character
                if move not in constants.LETTERS:  # the user entered an invalid letter (such as @, #, or $)
                    print(self.colorful.color_text("red", "Guesses should be letters. Please try again.\n"))
                elif move in self.board.guessed_letters:  # this letter has already been guessed
                    print(self.colorful.color_text("red", f"{move} has already been guessed. Please try again.\n"))
                elif move in constants.VOWELS and player.prize_money < constants.VOWEL_COST:  # if it's a vowel, we need to be sure the player has enough
                    print(self.colorful.color_text("red", f"You need ${constants.VOWEL_COST} to guess a vowel. Please try again.\n"))
                else:
                    return move
            else:
                return move

    def process_move(self, letter, value, prize):
        print(self.colorful.color_text("green", f"{self.cur_player.name} guesses {letter}"))
        self.board.add_guessed_letter(letter)
        if letter in constants.VOWELS:
            self.cur_player.buy_vowel()
        count = self.board.phrase.count(letter)  # returns an integer with how many times this letter appears
        if count > 0:
            if count == 1:
                print(self.colorful.color_text("magenta", f"There is one {letter}"))
            else:
                print(self.colorful.color_text("magenta", f"There are {count} {letter}'s"))
            self.cur_player.add_earnings(count * value, prize)
            print(self.cur_player)
            if self.board.is_phrase_revealed():  # all of the letters have been guessed
                self.winner = self.cur_player
            return True  # this player gets to go again
        elif count == 0:
            print(self.colorful.color_text("red", f"There is no {letter}"))
            return False

    def print_game_result(self):
        result = f"\nThe phrase was {self.board.phrase}\n\n"
        if self.winner is not None:
            result += f"{self.winner.win_message()}\n"
        else:
            result += "Nobody won.\n"
        print(self.colorful.color_text("magenta", result))

    def play(self):
        self.init_game()
        continue_cur_player = False  # at the beginning of the game, we don't have any current player
        while self.winner is None:
            self.print_board()
            if not continue_cur_player:
                self.set_cur_player()
            print(self.cur_player)
            # spin wheel and process the result
            spin_result = self.spin_wheel()
            if spin_result.typ == SpinResultType.BANKRUPT:
                self.cur_player.go_bankrupt()
                continue_cur_player = False
            elif spin_result.typ == SpinResultType.LOSE_TURN:
                continue_cur_player = False
            elif spin_result.typ == SpinResultType.CASH:
                move = self.request_move(self.cur_player)
                if move == "EXIT":
                    print(self.colorful.color_text("magenta", "\nBye!"))
                    break
                elif move == "PASS":
                    print(self.colorful.color_text("green", f"{self.cur_player.name} passes"))
                    continue_cur_player = False
                elif len(move) == 1:  # they guessed a letter
                    continue_cur_player = self.process_move(move, spin_result.value, spin_result.prize)
                else:  # they guessed the whole phrase
                    if move == self.board.phrase:  # they guessed the full phrase correctly
                        self.winner = self.cur_player
                        self.cur_player.add_earnings(spin_result.value, spin_result.prize)
                    else:
                        print(self.colorful.color_text("red", f"{move} was not the phrase"))
                        continue_cur_player = False
            time.sleep(2)
        self.print_game_result()


# Repeatedly asks the user for a number between min & max (inclusive)
def get_number_between(prompt, min_limit, max_limit):
    user_input = input(prompt)  # ask the first time
    while True:
        try:
            n = int(user_input)  # try casting to an integer
            if n < min_limit:
                error_message = f"Must be at least {min_limit}"
            elif n > max_limit:
                error_message = f"Must be at most {max_limit}"
            else:
                return n
        except ValueError:  # The user didn't enter a number
            error_message = f"{user_input} is not a number."
        # If we haven't gotten a number yet, add the error message and ask again
        user_input = input(f"{error_message}\n{prompt}")


if __name__ == "__main__":
    wof = WheelOfFortune(wheel_file="data/wheel.json", phrases_file="data/phrases.json")
    wof.play()
