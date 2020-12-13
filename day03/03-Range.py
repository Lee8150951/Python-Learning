# 只传入两个参数
oneToFive = list(range(1, 6))
for num in oneToFive:
    print(num)

# 传入三个参数
oneToTenDouble = list(range(1, 11, 2))
for num in oneToTenDouble:
    print(num)

# 先创建列表后使用.append 方法进行填入
squares = []
for value in range(1, 20, 4):
    squares.append(value)
print(squares)

# 解析列表
LongNum = [value ** 2 for value in range(1, 20)]
print(LongNum)