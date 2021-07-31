class Room:

    def __init__(self, room_name, capacity, entry_fee):
        self.room_name = room_name
        self.capacity = capacity
        self.entry_fee = entry_fee
        self.cash_register = 10000
        self.guests = []
        self.songs =[]

    def count_guests_in_room(self):
        return len(self.guests)

    def free_space_in_room(self):
        return self.capacity - len(self.guests)
    
    def take_entry_fee(self, entry_fee):
        self.cash_register += entry_fee

#     def check_in_guest_to_room(self, guest, room):
#         self.take_entry_fee(self, self.entry_fee)
#         self.guests.append(guest)
#         add

    def add_guest_to_room(self, guest):
        if self.capacity >= len(self.guests):
            self.guests.append(guest)
        else:
            return "Sorry, this room is taken"
    

    


