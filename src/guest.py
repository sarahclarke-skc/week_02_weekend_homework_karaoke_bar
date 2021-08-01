from src.bar_tab import BarTab


class Guest:

    def __init__(self, name, age, wallet, song):
        self.name = name
        self.age = age
        self.wallet = wallet
        self.favourite_song = song
    
    def can_afford_entry(self, amount):
        if self.wallet >= amount:
            return True
        else:
            return False
    
    def pay_for_entry(self, amount):
        self.wallet -= amount
    
    def guest_pays_tab_total(self, amount):
        self.wallet -= amount

 