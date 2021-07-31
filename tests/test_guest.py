import unittest

from src.guest import Guest
from src.room import Room
from src.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("John Lennon", 20, 20000)
        self.guest2 = Guest("Ringo Starr", 20, 23000)
        self.guest3 = Guest("Paul McCartney", 18, 15000)
        self.guest4 = Guest("George Harrison", 17, 500)
        self.guests = [self.guest1, self.guest2, self.guest3, self.guest4]

        # self.karaoke = Karaoke("Codeclan Caraoke", 1000)
        self.room1 = Room("The Ratpack", 3, 1000)
    
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
    