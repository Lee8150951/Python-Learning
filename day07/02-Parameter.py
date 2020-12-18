# P122练习
# 练习8-3
def make_shirt_1(size, string):
    print(f"Size:\"{size}\";String:\"{string}\"")
make_shirt_1(string = 'Python', size = 'L')
# 练习8-4
def make_shirt_2(string = 'Python'):
    print(f"I love {string}")
make_shirt_2()
make_shirt_2("JavaScript")
# 练习8-5
def describe_city(city = 'Shanghai', country = 'China'):
    print(f"{city.title()} is in {country.title()}.")
describe_city()
describe_city('New York', 'the U.S.A')
describe_city('Tokyo', 'Japan')