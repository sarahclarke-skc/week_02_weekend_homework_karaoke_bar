class Guest:

    def __init__(self, name, age, wallet):
        self.name = name
        self.age = age
        self.wallet = wallet
        self.favourite_song = ""
    
    def can_afford_entry(self, amount):
        if self.wallet >= amount:
            return True
        else:
            return False
    
    def pay_for_entry(self, amount):
        self.wallet -= amount
    
    # def fave_song_comes_on(self, song):
    #     if self.favourite_song == song:
    #             return "Let me sing!"