import unittest

from src.guest import Guest
from src.bar_tab import BarTab
from src.room import Room

class TestBarTab(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("John Lennon", 20, 20000, "Satisfaction")
        self.guest2 = Guest("Ringo Starr", 20, 23000, "Daydream Believer")
        self.guest4 = Guest("George Harrison", 17, 500, "Kokomo")

        self.room1 = Room("The Ratpack", 3, 1000)

        self.crisps = ["Ready Salted", "Cheese and Onion", "Salt and Vinegar"]
# shooting in the dark for the PDA dictionary
        self.drinks_menu = [
            {
                "name" : "Tennents",
                "alcohol_type" : "Lager",
                "price" : 300
            },
            {
                "name" : "Carling",
                "alcohol_type" : "Lager",
                "price" : 350
            },
            {
                "name" : "Merlot",
                "alcohol_type" : "Wine",
                "price" : 500
            },
            {
                "name" : "White Russian",
                "alcohol_type" : "Cocktail",
                "price" : 1000
            }
        ]

        self.bar_tab1 = BarTab("John Lennon", Room("The Ratpack", 3, 1000), self.drinks_menu)

    def test_bar_tab_has_guest(self):
        self.assertEqual("John Lennon", self.bar_tab1.guest)
    
    def test_bar_tab_has_tab_list(self):
        self.assertEqual([], self.bar_tab1.tab_list)
    
    def test_bar_tab_start_with_zero(self):
        self.assertEqual(0, self.bar_tab1.tab_total)

    def test_legal_sale_true(self):
        guest = self.guest1
        self.assertEqual(True, self.bar_tab1.legal_sale(guest))

    def test_legal_sale_false(self):
        guest = self.guest4
        self.assertEqual(False, self.bar_tab1.legal_sale(guest))

    def test_add_to_tab_list(self):
        guest = self.guest1
        self.bar_tab1.add_item_to_tab_list(self.drinks_menu[0])
        self.bar_tab1.add_item_to_tab_list(self.drinks_menu [1])
        self.assertEqual(2, len(self.bar_tab1.tab_list))

    # @unittest.skip("delete this line to run the test")
    def test_sum_tab_total(self):
        self.bar_tab1.add_item_to_tab_list(self.drinks_menu[0])
        self.bar_tab1.add_item_to_tab_list(self.drinks_menu [1])
        self.bar_tab1.sum_total_tab()
        self.assertEqual(650, self.bar_tab1.tab_total)
    
    def test_clear_tab_list(self):
        self.bar_tab1.add_item_to_tab_list(self.drinks_menu[0])
        self.bar_tab1.add_item_to_tab_list(self.drinks_menu [1])
        self.bar_tab1.clear_tab_list()
        self.assertEqual([], self.bar_tab1.tab_list)
    
    def test_take_bar_tab_payment(self):
        bar_tab = 1000
        self.room1.take_bar_tab_payment(bar_tab)
        self.assertEqual(11000, self.room1.cash_register)

    def test_bar_tab_transaction(self):
        self.bar_tab1.add_item_to_tab_list(self.drinks_menu[0])
        self.bar_tab1.add_item_to_tab_list(self.drinks_menu [1])
        self.bar_tab1.bar_tab_transaction(self.guest1, self.room1)
        self.assertEqual(19350, self.guest1.wallet)
        self.assertEqual(10650, self.room1.cash_register)
        self.assertEqual([], self.bar_tab1.tab_list)
        self.assertEqual(0, self.bar_tab1.tab_total)

# following not working --> cash register still increases
    # @unittest.skip("delete this line to run the test")
    def test_bar_tab_transaction_insuffient(self):
        self.bar_tab1.add_item_to_tab_list(self.drinks_menu[0])
        self.bar_tab1.add_item_to_tab_list(self.drinks_menu [1])
        self.bar_tab1.bar_tab_transaction(self.guest4, self.room1)
        self.assertEqual(500, self.guest4.wallet)
        self.assertEqual(10000, self.room1.cash_register)
        self.assertEqual(2, len(self.bar_tab1.tab_list))
        self.assertEqual(0, self.bar_tab1.tab_total)
