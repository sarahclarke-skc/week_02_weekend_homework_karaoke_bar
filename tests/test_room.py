import unittest

from src.karaoke import Karaoke
from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("The Ratpack", 5)
    
    def test_room_has_name(self):
        self.assertEqual("The Ratpack", self.room.room_name)

    def test_room_has_capacity(self):
        self.assertEqual(5, self.room.capacity)