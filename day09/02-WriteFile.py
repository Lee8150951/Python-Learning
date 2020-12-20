# P173练习
# 练习10-3
import os
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, "guest.txt")
with open(filename, 'w') as guest:
    while True:
        item = input("Please input your name or quit: ")
        if item == "quit":
            break
        else:
            guest.write(f"{item}\n")
# 练习10-4略方法同上
# 练习10-5略方法同上