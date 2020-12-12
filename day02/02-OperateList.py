bicycles = ['trek', 'cannondale', 'redline']
# 修改元素
bicycles[0] = "honda"
print(bicycles[0])
# 添加元素
bicycles.append("honda")
print(bicycles[-1])
bicycles.insert(0, 'lexus')
print(bicycles)
# 删除元素
bicycles.pop()
print(bicycles)
bicycles.pop(0)
print(bicycles)
bicycles.remove('cannondale')
print(bicycles)
del bicycles[0]
print(bicycles)