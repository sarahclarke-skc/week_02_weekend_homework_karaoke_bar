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
    
    def take_entry_fee(self, entry_fee):
        self.cash_register += entry_fee

    def add_guest_to_room(self, guest):
        if self.capacity >=len(self.guests):
            self.guests.append(guest)
        else:
         return "Sorry, this room is full."
        
# #check guest's money
# #check space in room
# #take money
# #add guest to room
#     def full_check_in_to_room(self, guest, room):
#         if self.free_space_in_room() == True and guest.can_afford_entry(room.entry_fee):
#             self.add_guest_to_room(guest)
#             self.take_entry_fee(room.entry_fee)
#             guest.pay_for_entry(guest)

        

