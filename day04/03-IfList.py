# P78练习
# 练习5-8
users = ['admin', 'mike', 'jacob', 'trump', 'zoe']
for user in users:
    if user == "admin":
        print("Hey, admin! Welcome back")
    else:
        print(f"Hey, {user}!")

# 练习5-9
users.clear()
if users:
    for user in users:
        if user == "admin":
            print("Hey, admin! Welcome back")
        else:
            print(f"Hey, {user}!")
else:
    print("We need more users!")

# 练习5-10
current_users = ['admin', 'mike', 'jacob', 'trump', 'zoe']
new_users = ['admin', 'mike', 'jack', 'rose', 'jane']
for user in new_users:
    if user in current_users:
        print("You should use an another username!")
    else:
        print("This name is OK!")

# 练习5-11
numList = list(range(1, 10))
i = 0
for num in numList:
    i = i + 1
    if num == 1:
        numList[i - 1] = "1st"
    elif num == 2:
        numList[i - 1] = "2nd"
    elif num == 3:
        numList[i - 1] = "3rd"
    else:
        numList[i - 1] = f"{num}th"
print(numList)