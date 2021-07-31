import unittest

# from src.karaoke import Karaoke
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
        
        self.guests_in_room = []
    
    def test_room_has_name(self):
        self.assertEqual("The Ratpack", self.room1.room_name)

    def test_room_has_capacity(self):
        self.assertEqual(3, self.room1.capacity)
    
    def test_room_has_entry_fee(self):
        self.assertEqual(1000, self.room1.entry_fee)

    def test_room_starts_with_no_guests(self):
        num_guests_in_room = self.room1.count_guests_in_room()
        self.assertEqual(0, num_guests_in_room)
    
    def test_free_spaces(self):
        free_spaces = self.room1.free_space_in_room()
        self.assertEqual(3, free_spaces)
    
    def test_add_guest_to_room(self):
        self.room1.add_guest_to_room(self.guest1)
        self.room1.add_guest_to_room(self.guest2)
        self.assertEqual(2, len(self.room1.guests))
    
    def test_room_full(self):
        self.room1.add_guest_to_room(self.guest1)
        self.room1.add_guest_to_room(self.guest2)
        self.room1.add_guest_to_room(self.guest3)
        self.room1.add_guest_to_room(self.guest4)
        self.assertEqual("Sorry, this room is taken", self.room1.add_guest_to_room(self.guest4))
    
    #test remove guest from room
    #add songs to rooms