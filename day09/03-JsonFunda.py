import json
import os
numbers = [2, 3, 5, 7, 11, 13]
here = os.path.dirname(os.path.abspath(__file__))
# 存储
filename = os.path.join(here, "numbers.json")
with open(filename, "w") as f:
    json.dump(numbers, f)

# 获取
with open(filename) as f:
    json_nums = json.load(f)
print(json_nums)