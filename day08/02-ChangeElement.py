# P149练习
# 练习9-4
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
restaurant = Restaurant("Yoshino home", "Japanese cuisine")
restaurant.set_number_served(30)
print(restaurant.number_served)
restaurant.increment_number_served(20)
print(restaurant.number_served)
# 练习9-5 略方法同上