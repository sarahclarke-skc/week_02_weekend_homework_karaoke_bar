class Room:

    def __init__(self, room_name, capacity, entry_fee):
        self.room_name = room_name
        self.capacity = capacity
        self.entry_fee = entry_fee
        self.cash_register = 10000
        self.guests = []
        self.playlist =[]

    def count_guests_in_room(self):
        return len(self.guests)
    
    def take_entry_fee(self, entry_fee):
        self.cash_register += entry_fee

    def add_guest_to_room(self, guest):
        if self.capacity >=len(self.guests):
            self.guests.append(guest)
        else:
         return "Sorry, this room is full."

    def full_check_in_to_room(self, guest):
        if self.capacity >= len(self.guests) and guest.can_afford_payment(self.entry_fee):
            guest.pay_for_entry(self.entry_fee)
            self.cash_register += self.entry_fee
            self.add_guest_to_room(guest)

    def check_out_guest(self, guest):
        for item in self.guests:
            if item == guest:
                self.guests.remove(guest)
        else:
            return "This guest isn't in this room."
    
    def add_song_to_room(self, song):
        self.playlist.append(song)
    
    def add_songs_to_room(self, songs):
        for song in songs:
            self.playlist.append(song)
    
    def is_guest_in_room(self, guest):
        return guest in self.guests
    
    def guest_reaction(self, guest):
        if guest.favourite_song in self.playlist:
            return "Woohoo! Pass me the mic!"
        else:
             return "We should have gone somewhere else!"

    def take_bar_tab_payment(self, amount):
        self.cash_register += amount


        
