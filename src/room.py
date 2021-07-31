class Room:

    def __init__(self, room_name, capacity):
        self.room_name = room_name
        self.capacity = capacity
        self.guests = []
        self.songs =[]

    def count_guests_in_room(self):
        return len(self.guests)

    def free_space_in_room(self):
        return self.capacity - len(self.guests)

    def add_guest_to_room(self, guest):
        if self.capacity >= len(self.guests):
            self.guests.append(guest)
        else:
            return "Sorry, this room is taken"

