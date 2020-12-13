# P52练习
# 练习4-3
for num in range(1, 21):
    print(num)
# 练习4-4
List = list(range(1, 1000000))
for num in List:
    print(num)
# 练习4-5
print(min(List))
print(max(List))
print(sum(List))
# 练习4-6
oneToTwenty = list(range(1, 21, 2))
print(oneToTwenty)
# 练习4-7
threeToThirty = list(range(3, 31, 3))
print(threeToThirty)
# 练习4-8
cubics = []
for cubic in range(1, 11):
    cubics.append(cubic ** 3)
print(cubics)
# 练习4-9
cubics_2 = [cubic ** 3 for cubic in range(1, 11)]
print(cubics_2)