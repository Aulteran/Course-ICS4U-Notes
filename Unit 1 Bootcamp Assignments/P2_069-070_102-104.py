'''
Author: Aadil Hussain
Built on: Python 3.10.8
'''
# Bootcamp Assignments #2 - 069-070, 102-104 (DUE MON. SEPT. 18)

# 069
countries = ("china", "vietnam", "canada", "india", "iceland")
print(countries)
print(countries.index(input("enter one of the country names: ")))

# 070
print(countries[int(input("enter a number between 1 and 5"))+1])

# 102
ppls = []
for i in range(4):
    ppls.append({})
    ppls[i]['name'] = input(f"enter person{i} name: ")
    ppls[i]['age'] = input(f"enter person{i} age: ")
    ppls[i]['size'] = input(f"enter person{i} shoe size: ")
person = input("enter a persons name: ")
for i in ppls:
    if i['name'] == person:
        print(i)

# 103
for i in ppls:
    if i['name'] == person:
        print(f"{i['name']}, {i['age']}")

# 104
removeguy = input("enter guy name to remove: ")
for person in ppls:
    if person["name"]==removeguy:
        ppls.remove(person)
