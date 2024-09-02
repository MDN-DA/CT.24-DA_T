animals = {
    "Lion": "Cub",
    "Pigeon": "Squab",
    "Gecko": "Baby Gecko",
    "Hedgehog": "Hoglet"
}

print(animals["Gecko"])

animals["Gecko"] = "Hatchling"

print(animals["Gecko"])
print(animals.keys()) #Lion
print(animals.values()) #Cub
print(animals.items()) #qty
print(animals.get("Gecko")) #found
print(animals.get("Cat"))
print(animals.get("Cat", "This animal not listed"))
print(animals.setdefault("Lion", "Baby Lion"))

animals.setdefault("Zebra", "Foal") #if not available, it's add
print(animals)
animals.update({"Fish": "Fry", "Crab": "Zoea"}) #merges dico
print(animals)
animals.pop("Lion")
print(animals)
animals.popitem()
print(animals)