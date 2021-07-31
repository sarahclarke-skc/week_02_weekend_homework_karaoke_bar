import unittest

from src.karaoke import Karaoke
from src.room import Room
from src.song import Song
from src.guest import Guest

class TestKaraoke(unittest.TestCase):

    def setUp(self):
        self.karaoke = Karaoke("Codeclan Caraoke", 1000)
    
    def test_karaoke_bar_has_name(self):
        self.assertEqual("Codeclan Caraoke", self.karaoke.name)

    def test_karaoke_bar_has_entry_fee(self):
        self.assertEqual(1000, self.karaoke.entry_fee)

    def test_karaoke_bar_starts_with_no_guests(self):
        self.assertEqual(0, self.karaoke.count_guests())

    def test_karaoke_bar_takes_entry_fee(self):
        self.karaoke.take_entry_fee(self.karaoke.entry_fee)
        till_after_payment = self.karaoke.cash_register
        self.assertEqual(11000, till_after_payment)

    
    


    