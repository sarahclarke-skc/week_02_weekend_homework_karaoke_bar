import unittest

from src.karaoke import Karaoke
from src.room import Room
from src.song import Song
from src.guest import Guest

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("Satisfaction", "The Rolling Stones")
        self.song2 = Song("Daydream Believer", "The Monkees")
    
    def test_song_has_name(self):
        self.assertEqual("Satisfaction", self.song1.song_name)

    def test_song_has_artist(self):
        self.assertEqual("The Rolling Stones", self.song1.artist)