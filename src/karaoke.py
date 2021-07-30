class Karaoke:

    def __init__(self, name):
        self.name = name
        self.entry_fee = 1000

    def can_afford_entry(self, guest):
        if guest.wallet >= self.entry_fee:
            return True
        else:
            return False