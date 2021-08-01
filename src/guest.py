from src.bar_tab import BarTab


class Guest:

    def __init__(self, name, age, wallet, song):
        self.name = name
        self.age = age
        self.wallet = wallet
        self.favourite_song = song
    
    def can_afford_payment(self, amount):
        if self.wallet >= amount:
            return True
        else:
            return False
    
    def pay_for_entry(self, amount):
        if self.can_afford_payment(amount) == True:
            self.wallet -= amount
        else:
            return "Insufficient funds"
    
    def guest_pays_tab_total(self, amount):
        if self.can_afford_payment(amount) == True and self.age >= 18:
            self.wallet -= amount
        else:
            return "Insufficient funds"

 