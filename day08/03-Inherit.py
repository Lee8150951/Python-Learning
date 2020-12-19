# P155练习
# 练习9-6
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(f"{self.restaurant_name} => {self.cuisine_type}")
    def open_restaurant(self):
        print("It\'s opening, welcome!")
    def set_number_served(self, number_served):
        self.number_served = number_served
    def increment_number_served(self, add_served):
        self.number_served = self.number_served + add_served

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["KFC", "BurgerKing", "Mc Donald", "PizzaHut"]
    def show_flavors(self):
        for flavor in self.flavors:
            print(flavor)

IceCreams = IceCreamStand("Yoshino home", "Japanese cuisine")
IceCreams.show_flavors()
# 练习9-7 略方法同上
# 练习9-8
class Icecream:
    def __init__(self, ice_color, price):
        self.ice_color = ice_color
        self.price = price

class IceCreamStore(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["KFC", "BurgerKing", "Mc Donald", "PizzaHut"]
        self.icecream = Icecream("white", 30)
    def show_flavors(self):
        for flavor in self.flavors:
            print(flavor)
icecream_store = IceCreamStore("Yoshino home", "Japanese cuisine")
color = icecream_store.icecream.ice_color
print(color)
# 练习9-9 略方法同上