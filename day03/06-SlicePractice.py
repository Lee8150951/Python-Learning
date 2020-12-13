# P57练习
tourists = ['Shanghai', 'Shaanxi', 'Tibet', 'Sichuan', 'Xinjiang']
# 练习4-10
tourists_1 = tourists[:3]
print("The first three items in the list are:")
for tourist in tourists_1:
    print(tourist)
tourists_2 = tourists[1:4]
print("Three items from the middle of the list are:")
for tourist in tourists_2:
    print(tourist)
tourists_3 = tourists[2:]
print("The last three items in the list are:")
for tourist in tourists_3:
    print(tourist)
# 练习4-11
pizzas = ['pizza hut', 'pop john', 'the butchers']
friend_pizzas = pizzas[:]
print(friend_pizzas)
# 练习4-12
for item in pizzas:
    print(item)
for item in friend_pizzas:
    print(item)