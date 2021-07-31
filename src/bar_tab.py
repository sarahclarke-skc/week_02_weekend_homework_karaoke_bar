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

  # Can't get the test to pass --> list indices must be intergers or slices
    # def sum_total_tab(self):
    #    self.tab_total += self.tab_list["price"]
        