# P134练习
# 练习8-12
def make_sandwich(*ingredient):
    print(ingredient)
make_sandwich("hotdog", "bread", "vegetable")
# 练习8-11
def build_profile(first_name, last_name, **info):
    print(info)
build_profile("Jacob", "Lee", core = 100, age = 22)
# 练习8-12 略方法同上