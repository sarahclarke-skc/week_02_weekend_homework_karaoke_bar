class Karaoke:

    def __init__(self, name, entry_fee):
        self.name = name
        self.entry_fee = entry_fee
        self.cash_register = 10000
        self.guests = []

    def take_entry_fee(self, entry_fee):
        self.cash_register += entry_fee