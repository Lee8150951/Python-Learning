# P104练习
# 练习7-1
brand = input("Please enter the brand of the vehicle you want: ")
print(f"Let me see if I can find you a {brand.title()}")
# 练习7-2
num = input("How many people eat: ")
if int(num) > 8:
    print("There\'s no seat.")
else:
    print("Welcome!")
# 练习7-3
numToTest = input("Please input a number: ")
flag = (int(numToTest) % 10 == 0)
if flag:
    print("yes")
else:
    print("no")