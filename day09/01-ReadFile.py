# P171练习
# 练习10-1
import os
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, "learning_python.txt")
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line)
# 练习10-2
for item in lines:
    item = item.replace("Python", "JavaScript")
    print(item)