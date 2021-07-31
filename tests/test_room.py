import unittest

from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room("The Ratpack", 3, 1000)
        self.room2 = Room("The Beach Boys", 10, 5000)
        self.room3 = Room('The Everly Brothers', 8, 3000)
        rooms = [self.room1, self.room2, self.room3]

        self.guest1 = Guest("John Lennon", 20, 20000)
        self.guest2 = Guest("Ringo Starr", 20, 23000)
        self.guest3 = Guest("Paul McCartney", 18, 15000)
        self.guest4 = Guest("George Harrison", 17, 500)
        
        self.guests = []
    
    def test_room_has_name(self):
        self.assertEqual("The Ratpack", self.room1.room_name)

    def test_get_capacity(self):
        self.assertEqual(3, self.room1.capacity)
    
    def test_get_room_entry_fee(self):
        self.assertEqual(1000, self.room1.entry_fee)

    def test_room_starts_with_no_guests(self):
        num_guests_in_room = len(self.room1.guests)
        self.assertEqual(0, num_guests_in_room)
    
    def test_count_guests_in_room(self):
        self.assertEqual(0, self.room1.count_guests_in_room())

    def test_add_guest_to_room(self):
        self.room1.add_guest_to_room(self.guest1)
        self.assertEqual(1, len(self.room1.guests))

    def test_add_guest_to_room_too_full(self):
        self.room1.add_guest_to_room(self.guest1)
        self.room1.add_guest_to_room(self.guest2)
        self.room1.add_guest_to_room(self.guest3)
        self.room1.add_guest_to_room(self.guest4)
        self.assertEqual("Sorry, this room is full.", self.room1.add_guest_to_room(self.guest4))
        
    def test_room_takes_entry_fee(self):
        self.room1.take_entry_fee(self.room1.entry_fee)
        till_after_payment = self.room1.cash_register
        self.assertEqual(11000, till_after_payment)

    

    # def test_full_check_in_to_room(self):
    #     guest = self.guest1
    #     room = self.room1
    #     room.full_check_in_to_room(guest, room)
    #     self.assertEqual(True, guest.can_afford_entry(room.entry_fee))
    #     self.assertEqual(19000, guest.wallet)
    #     self.assertEqual(1, len(room.guests))
    #     self.assertEqual(11000, self.room1.cash_register)
        
    #test remove guest from room
    #add songs to rooms