# P100练习
# 练习6-7
man_1 = {'first_name': 'Jacob', 'last_name': 'Lee', 'age': 22, 'city': 'Shanghai'}
man_2 = {'first_name': 'Abby', 'last_name': 'Shia', 'age': 24, 'city': 'Shanghai'}
man_3 = {'first_name': 'Tom', 'last_name': 'Cruise', 'age': 52, 'city': 'Los Angle'}
mans = [man_1, man_2, man_3]
for man in mans:
    print(man)
# 练习6-8 略方法同上
# 练习6-9
favorite_places = {
    'Jacob': ['Shanghai', 'Nanchang', 'Chengdu', 'Tokyo'],
    'Abby': ['Shanghai', 'Suzhou', 'Chongqing'],
    'Tom': ['Los Angle', 'Beijing', 'New York']
}
for name, citys in favorite_places.items():
    print(f"{name} like:")
    for city in citys:
        print(f"\t{city}")
# 练习6-10 略方法同上
# 练习6-11
cities = {
    'Shanghai': {
        'country': 'China',
        'polpulation': '24281400',
        'rank': 5
    },
    'Tokyo': {
        'country': 'Japan',
        'polpulation': '13920000',
        'rank': 9
    },
    'Seoul': {
        'country': 'Korea',
        'population': '10040000',
        'rank': 10
    },
    'New York': {
        'country': 'USA',
        'population': '8510000',
        'rank': 1
    }
}
for city, info in cities.items():
    print(f"{city}\'s information=>")
    for key, value in info.items():
        print(f"\t{key}: {value}")