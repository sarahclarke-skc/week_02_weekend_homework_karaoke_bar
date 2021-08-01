import unittest

from src.guest import Guest
from src.room import Room
from src.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("John Lennon", 20, 20000, "Satisfaction")
        self.guest2 = Guest("Ringo Starr", 20, 23000, "Daydream Believer")
        self.guest3 = Guest("Paul McCartney", 18, 15000, "Hoochie Coochie Man")
        self.guest4 = Guest("George Harrison", 17, 500, "Kokomo")
        self.guests = [self.guest1, self.guest2, self.guest3, self.guest4]

        # self.karaoke = Karaoke("Codeclan Caraoke", 1000)
        self.room1 = Room("The Ratpack", 3, 1000)

        self.song1 = Song("Satisfaction", "The Rolling Stones")
        self.song2 = Song("Daydream Believer", "The Monkees")
    
    def test_guest_has_name(self):
        self.assertEqual("John Lennon", self.guest1.name)
    
    def test_guest_has_age(self):
        self.assertEqual(20, self.guest1.age)
    
    def test_guest_has_wallet(self):
        self.assertEqual(20000, self.guest1.wallet)
    
    def test_guest_can_afford_entry_true(self):
        entry_fee = self.room1.entry_fee
        can_afford_entry = self.guest1.can_afford_entry(entry_fee)
        self.assertEqual(True, can_afford_entry)

    def test_guest_can_afford_entry_false(self):
        entry_fee = self.room1.entry_fee
        can_afford_entry = self.guest4.can_afford_entry(entry_fee)
        self.assertEqual(False, can_afford_entry)
    
    def test_guest_pays_for_entry(self):
        amount = self.room1.entry_fee
        self.guest1.pay_for_entry(amount)
        wallet = self.guest1.wallet
        self.assertEqual(19000, wallet)

    def test_guest_pays_for_entry_insufficient(self):
        amount = self.room1.entry_fee
        guest_cannot_pay = self.guest4.pay_for_entry(amount)
        self.assertEqual(None, guest_cannot_pay)
    
    def test_guest_has_favourite_song(self):
        self.assertEqual("Satisfaction", self.guest1.favourite_song)

    
    # def test_guest_finds_song_in_room(self):
    #     song = self.guest1.favourite_song
    #     find_song = self.guest1.find_song_in_room(song)
    #     self.songs = [self.song1, self.song2]
    #     self.guest1.find_song_in_room(song)
    #     self.assertEqual("Woohoo! Pass me the mic!", find_song)