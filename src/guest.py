class Guest:

    def __init__(self, name, age, wallet):
        self.name = name
        self.age = age
        self.wallet = wallet
    
    def can_afford_entry(self, karaoke):
        if self.wallet >= karaoke.entry_fee:
            return True
        else:
            return False
    
    def pay_for_entry(self, karaoke):
        self.can_afford_entry(karaoke)
        self.wallet -= karaoke.entry_fee