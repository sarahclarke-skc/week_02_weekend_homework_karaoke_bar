class Guest:

    def __init__(self, name, age, wallet):
        self.name = name
        self.age = age
        self.wallet = wallet
    
    def can_afford_entry(self, room):
        if self.wallet >= room.entry_fee:
            return True
        else:
            return False
    
    def pay_for_entry(self, room):
        self.can_afford_entry(room)
        self.wallet -= room.entry_fee