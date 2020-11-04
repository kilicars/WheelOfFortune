import constants


class Player:
    def __init__(self, name):
        self.name = name
        self.prize_money = 0
        self.prizes = []

    def add_money(self, money):
        self.prize_money += money

    def go_bankrupt(self):
        self.prize_money = 0

    def buy_vowel(self):
        self.prize_money -= constants.VOWEL_COST

    def add_prize(self, prize):
        self.prizes.append(prize)

    def add_earnings(self, money, prize):
        self.add_money(money)
        if prize:
            self.add_prize(prize)

    def win_message(self):
        message = f"{self.name} wins!\n"
        message += f"{self.name} won ${self.prize_money}\n"
        if len(self.prizes) > 0:
            message += f"{self.name} also won:\n"
            for prize in self.prizes:
                message += f"    * {prize}\n"
        return message

    def __str__(self):
        return f"{self.name} has ${self.prize_money}"
