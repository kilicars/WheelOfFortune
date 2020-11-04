import json
import random
from enum import Enum


class SpinResultType(Enum):
    CASH = "cash"
    BANKRUPT = "bankrupt"
    LOSE_TURN = "lose_turn"


class SpinResult:
    def __init__(self, typ, text, value, prize):
        self.typ = typ
        self.text = text
        self.value = value
        self.prize = prize


class Wheel:
    def __init__(self, file):
        self.file = file
        self.wheel = self.init_wheel()

    def init_wheel(self):
        with open(self.file, "r") as f:
            wheel = json.loads(f.read())
            return wheel

    # Spins the wheel of fortune wheel to give a random prize
    # Examples:
    #    { "type": "cash", "text": "$950", "value": 950, "prize": "A trip to Ann Arbor!" },
    #    { "type": "bankrupt", "text": "Bankrupt", "prize": false },
    #    { "type": "loseturn", "text": "Lose a turn", "prize": false }
    def spin(self):
        value = 0
        typ = None
        result = random.choice(self.wheel)
        if result["type"] == "cash":
            typ = SpinResultType.CASH
            value = result["value"]
        elif result["type"] == "bankrupt":
            typ = SpinResultType.BANKRUPT
        elif result["type"] == "lose_turn":
            typ = SpinResultType.LOSE_TURN
        text = result["text"]
        prize = result["prize"]
        return SpinResult(typ, text, value, prize)
