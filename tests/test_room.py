import unittest

from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room("The Ratpack", 3, 1000)
        self.room2 = Room("The Beach Boys", 10, 5000)
        self.room3 = Room('The Everly Brothers', 8, 3000)
        self.rooms = [self.room1, self.room2, self.room3]

        self.guest1 = Guest("John Lennon", 20, 20000, "Satisfaction")
        self.guest2 = Guest("Ringo Starr", 20, 23000, "Daydream Believer")
        self.guest3 = Guest("Paul McCartney", 18, 15000, "Hoochie Coochie Man")
        self.guest4 = Guest("George Harrison", 17, 500, "Kokomo")

        self.song1 = Song("Satisfaction", "The Rolling Stones")
        self.song2 = Song("Daydream Believer", "The Monkees")
        self.songs = [self.song1, self.song2]

    def test_room_has_name(self):
        expected = "The Ratpack"
        actual = self.room1.room_name
        self.assertEqual(expected, actual)

    def test_get_capacity(self):
        expected = 3
        actual = self.room1.capacity
        self.assertEqual(expected, actual)
    
    def test_get_room_entry_fee(self):
        expected = 1000
        actual = self.room1.entry_fee
        self.assertEqual(expected, actual)

    def test_room_starts_with_no_guests(self):
        num_guests_in_room = len(self.room1.guests)
        self.assertEqual(0, num_guests_in_room)
    
    def test_count_guests_in_room(self):
        self.assertEqual(0, self.room1.count_guests_in_room())

    def test_add_guest_to_room(self):
        self.room1.add_guest_to_room(self.guest1)
        self.assertEqual(1, len(self.room1.guests))

    def test_add_guest_to_room_too_full(self):
        self.room1.add_guest_to_room(self.guest1)
        self.room1.add_guest_to_room(self.guest2)
        self.room1.add_guest_to_room(self.guest3)
        self.room1.add_guest_to_room(self.guest4)
        self.assertEqual("Sorry, this room is full.", self.room1.add_guest_to_room(self.guest4))
        
    def test_room_takes_entry_fee(self):
        self.room1.take_entry_fee(self.room1.entry_fee)
        till_after_payment = self.room1.cash_register
        self.assertEqual(11000, till_after_payment)

    def test_full_check_in_to_room(self):
        guest = self.guest1
        room = self.room1
        room.full_check_in_to_room(guest)
        self.assertEqual(11000, room.cash_register)
        self.assertEqual(19000, guest.wallet)
        self.assertEqual(1, len(room.guests))
        # self.assertEqual(["John Lennon"], self.room1.guests)
        
    def test_check_out_guest(self):
        self.room1.full_check_in_to_room(self.guest1)
        self.room1.full_check_in_to_room(self.guest2)
        self.assertEqual(2,len(self.room1.guests))
        self.room1.check_out_guest(self.guest1)
        self.assertEqual(1, len(self.room1.guests))
    
    def test_check_out_guest_not_present(self):
        self.assertEqual("This guest isn't in this room.", self.room1.check_out_guest(self.guest4))

    def test_add_song_to_room(self):
        self.room1.add_song_to_room(self.song1)
        self.assertEqual(1, len(self.room1.playlist))

    def test_add_songs_to_room(self):
        songs = [self.song1, self.song2]
        self.room1.add_songs_to_room(songs)
        self.assertEqual(2, len(self.room1.playlist))
    
    # def test_find_song_by_title(self):
    #     self.room1.add_songs_to_room(self.songs)
    #     song = self.room1.find_song_by_title("Satisfaction")
    #     self.assertEqual(self.song1.song_name, song)
