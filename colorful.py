from colorama import Fore, init


class Colorful:
    def __init__(self):
        init(strip=False)
        self.colors = {
            "blue": Fore.BLUE,
            "green": Fore.GREEN,
            "magenta": Fore.MAGENTA,
            "red": Fore.RED,
            "yellow": Fore.YELLOW,
            "cyan": Fore.CYAN
        }
        self.reset = Fore.RESET

    def color_text(self, color, text):

        return f"{self.colors[color]}{text}{self.reset}"
