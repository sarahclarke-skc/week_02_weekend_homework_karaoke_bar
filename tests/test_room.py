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
    
    def test_room_has_name(self):
        self.assertEqual("The Ratpack", self.room1.room_name)

    def test_room_has_capacity(self):
        self.assertEqual(5, self.room1.capacity)