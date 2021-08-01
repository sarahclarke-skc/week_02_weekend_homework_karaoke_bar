class BarTab:
    def __init__(self, guest, room, drinks_menu):
        self.guest = guest
        self.room = room
        self.drinks_menu = drinks_menu
        self.tab_total = 0
        self.tab_list = []
    
    def legal_sale(self, guest):
        if guest.age >= 18:
            return True
        else:
            return "You aren't old enough yet."
    
    def add_item_to_tab_list(self, item):
        self.tab_list.append(item)

    def sum_total_tab(self):
        self.tab_total = 0
        for item in self.tab_list:
            self.tab_total += item["price"]

    def clear_tab_list(self):
        self.tab_list.clear()

    def bar_tab_transaction(self, guest, room, bartab):
        bartab.sum_total_tab()
        guest.guest_pays_tab_total(bartab.tab_total)
        room.take_bar_tab_payment(bartab.tab_total)
        bartab.clear_tab_list()
        bartab.sum_total_tab()