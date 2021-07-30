import unittest

from src.guest import Guest
from src.karaoke import Karaoke
from src.room import Room
from src.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("John Lennon", 20, 20000)
        # self.guest2 = Guest("Ringo Starr", 20, 23000)
    
    def test_guest_has_name(self):
        self.assertEqual("John Lennon", self.guest.name)
    
    def test_guest_has_age(self):
        self.assertEqual(20, self.guest.age)
    
    def test_guest_has_wallet(self):
        self.assertEqual(20000, self.guest.wallet)
       