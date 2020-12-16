# P113练习
# 练习7-8
sandwich_orders = ['KFC', 'BGK', 'McD']
finished_sandwichds = []
while sandwich_orders:
    print("I made your tuna sandwich.")
    sandwich = sandwich_orders.pop()
    finished_sandwichds.append(sandwich)
print(finished_sandwichds)
# 练习7-9
sandwich_orders = ['KFC', 'pastrami', 'BGK', 'pastrami', 'pastrami', 'McD']
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)
# 练习7-10
hobbies = {}
while True:
    name = input("Please input your name: ")
    if name == 'quit':
        break
    hobby = input("Please input your hobby: ")
    hobbies[name] = hobby
print(hobbies)