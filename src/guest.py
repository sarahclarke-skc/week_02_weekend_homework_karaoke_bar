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

    # def guest_reaction(self, room, song):
    #         if song in room.playlist == self.favourite_song:
    #             return "Woohoo! Pass me the mic!"