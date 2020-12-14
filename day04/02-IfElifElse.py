# P75练习
# 练习5-3
alien_color = "green"
count = 0
if alien_color == "green":
    count = count + 5
print(count)

alien_color = "yellow"
count = 0
if alien_color == "red":
    count = count + 5
print(count)

# 练习5-4
alien_color = "red"
count = 0
if alien_color == "green":
    count = count + 5
else:
    count = count + 10
print(count)

# 练习5-5
alien_color = "red"
count = 0
if alien_color == "green":
    count = count + 5
elif alien_color == "red":
    count = count + 10
else:
    count = count + 20
print(count)

# 练习5-6
age = 30
if age < 2:
    print("baby")
elif age >= 2 and age < 4:
    print("infant")
elif age >= 4 and age < 13:
    print("children")
elif age >= 13 and age < 20:
    print("teenager")
elif age >= 20 and age < 65:
    print("adult")
elif age >= 65:
    print("elderly")

# 练习5-7
tourists = ['Shanghai', 'Shaanxi', 'Tibet', 'Sichuan', 'Xinjiang']
if "Shanghai" in tourists:
    print("You really like Shanghai!")