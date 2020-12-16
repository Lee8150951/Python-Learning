# P110练习
# 练习7-4
ingredient = ''
while ingredient != 'quit':
    ingredient = input("Please input an ingredient: ")
    print(ingredient)
# 练习7-5
while True:
    age = input("Please input your age: ")
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("free")
    elif age >= 3 and age < 12:
        print("$10")
    elif age >= 12:
        print("$15")
# 练习7-6 略
# 练习7-7
while 1:
    print("use Ctrl + C")