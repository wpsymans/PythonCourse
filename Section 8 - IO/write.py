weapons = ["Sword","Bow","Axe"]
with open("cities.txt",'w') as city_file:
    for weapon in weapons:
        print(weapon, file=city_file)