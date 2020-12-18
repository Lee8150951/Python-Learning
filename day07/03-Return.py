# P127练习
# 练习8-6
def city_country(city, country):
    conclusion = f"{city.title()}, {country.title()}"
    return conclusion
info = city_country("Santiago", "Chie")
print(info)
info = city_country("Shanghai", "China")
print(info)
info = city_country("Tokyo", "Japan")
print(info)
# 练习8-7
def make_album(singer_name, album_name, count):
    album = {
        "singer_name": singer_name,
        "album_name": album_name,
        "count": count
    }
    return album
album = make_album("Jay Chou", "Mdm Yeh Huimei", 20)
print(album)
# 练习8-8
while True:
    singer_name = input("Singer\'s Name: ")
    album_name = input("Album\'s Name: ")
    count = input("Album\'s count: ")
    album = make_album(singer_name, album_name, count)
    quit = input("Do you want to quit(y/n): ")
    print(album)
    if quit == "y":
        break