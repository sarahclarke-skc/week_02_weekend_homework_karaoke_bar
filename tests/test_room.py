import unittest

from src.karaoke import Karaoke
from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room("The Ratpack", 5)
        self.room2 = Room("The Beach Boys", 10)
        self.room3 = Room('The Everly Brothers', 8)
        rooms = [self.room1, self.room2, self.room3]

        self.guest1 = Guest("John Lennon", 20, 20000)
        self.guest2 = Guest("Ringo Starr", 20, 23000)
        self.guest3 = Guest("Paul McCartney", 18, 15000)
        self.guest4 = Guest("George Harrison", 17, 500)
        # self.guests = [self.guest1, self.guest2, self.guest3, self.guest4]
        self.guests_in_room = []
    
    def test_room_has_name(self):
        self.assertEqual("The Ratpack", self.room1.room_name)

    def test_room_has_capacity(self):
        self.assertEqual(5, self.room1.capacity)

    def test_room_starts_with_no_guests(self):
        num_guests_in_room = self.room1.count_guests_in_room()
        self.assertEqual(0, num_guests_in_room)
    
    def test_free_spaces(self):
        free_spaces = self.room1.free_space_in_room()
        self.assertEqual(5, free_spaces)
    
    def test_add_guest_to_room(self):
        self.room1.add_guest_to_room(self.guest1)
        self.room1.add_guest_to_room(self.guest2)
        self.assertEqual(2, len(self.room1.guests))