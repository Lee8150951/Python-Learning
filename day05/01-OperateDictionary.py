# P88练习
# 练习6-1
man = {
    'first_name': 'Jacob',
    'last_name': 'Lee',
    'age': 22,
    'city': 'Shanghai'
}
print(man)
# 练习6-2 略
# 练习6-3
python = {
    'dictionary': 'it can store many Key/value pairs',
    'list': 'it can store many data, but they can be changed',
    'tuple': 'it can store many data, and they can\'t be changed'
}
dictionary = python.get('dictionary', 'can\' find')
list = python.get('list', 'can\' find')
tuple = python.get('tuple', 'can\' find')
print(f"dictionary=>{dictionary}")
print(f"list=>{list}")
print(f"tuple=>{tuple}")