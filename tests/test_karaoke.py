import unittest

from src.karaoke import Karaoke
from src.room import Room
from src.song import Song
from src.guest import Guest

class TestKaraoke(unittest.TestCase):

    def setUp(self):
        self.karaoke = Karaoke("Codeclan Caraoke")
    
    def test_karaoke_bar_has_name(self):
        self.assertEqual("Codeclan Caraoke", self.karaoke.name)

    def test_karaoke_bar_has_entry_fee(self):
        self.assertEqual(1000, self.karaoke.entry_fee)
    
    