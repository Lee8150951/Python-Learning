# P144练习
# 练习9-1
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"{self.restaurant_name} => {self.cuisine_type}")
    def open_restaurant(self):
        print("It\'s opening, welcome!")
restaurant = Restaurant("Yoshino home", "Japanese cuisine")
restaurant.describe_restaurant()
restaurant.open_restaurant()
# 练习9-2 略方法同上
# 练习9-3
class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def describe_user(self):
        print(f"{self.first_name.title()}{self.last_name.title()} => {self.age}")
    def greet_user(self):
        print(f"Hello, {self.first_name.title()}!")
usre_1 = User("Jacob", "Lee", 22)
usre_1.describe_user()
usre_1.greet_user()