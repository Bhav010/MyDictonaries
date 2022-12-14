phonebook = {"Chris": "555−1111", "Katie": "555−2222", "Joanne": "555−3333"}

"""
print()
print("*****  start section 1 - print dictionary ********")
print()


print(phonebook)
print(len(phonebook))

mydictionary = dict(m=8, n=9)
print(mydictionary)


print(phonebook["Chris"])
print(mydictionary["m"])

print()
print("*****  end section 1 ********")
print()


print()
print("*****  start section 2 - search dictionary ********")
print()


name = "Chri"

if name in phonebook:
    print(phonebook[name])
else:
    print(name, "is not in phonebook")


if (phonebook["Chris"]) in phonebook:
    print(phonebook["Chris"])
else:
    print(phonebook["Chris"]), "is not in phonebook)"


print()
print("*****  end section 2 ********")
print()



print()
print("*****  start section 3 - edit/append dictionary ********")
print()

print(phonebook)
phonebook["Joe"] = "555-0123"
phonebook["Chris"] = "555-4444"

print(phonebook)


print()
print("*****  end section 3 ********")
print()


print()
print("*****  start section 4 - delete/remove from dictionary ********")
print()

print(phonebook)
del phonebook["Chris"]
print(phonebook)


print()
print("*****  end section 4 ********")
print()


print()
print("*****  start section 5 - iterate through keys ********")
print()


for key in phonebook:
    print(key)
    print(phonebook[key])

print()
print("*****  end section 5 ********")
print()


print()
print("*****  start section 6 - iterate through values  ********")
print()


for v in phonebook.values():
    print(v)

print()
print("*****  end section 6 ********")
print()


print()
print("*****  start section 7 - iterate through both key and value pair********")
print()

for key, value in phonebook.items():
    print(key)
    print(value)

for item in phonebook.items():
    print(item)

for key, value in enumerate(phonebook):
    print(key)
    print(value)

print()
print("*****  end section 7 ********")
print()

print()
print("*****  start section 8 - using random and converting to list ********")
print()

phone = phonebook.get("Chris", "key not found")
print(phone)

print()
print("*****  remove key value out of dictionary ********")
print()

remove = phonebook.pop("chris", "not found")
print(remove)
print(phonebook)


a = phonebook.popitem()
print(a)
print(phonebook)


print()
print("*****  end section 8 ********")
print()

"""
import random

random_list = list(phonebook)
print(random_list)
random_key = random.choice(random_list)
print(random_key)
print(phonebook[random_key])

print(phonebook[random.choice(list(phonebook))])
