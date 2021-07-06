groceries = ["ham","spam","milk","bread"]

#this block removes spam from the grocery list using continue

for item in groceries:
    if item == "spam":
        continue
    print(item)

print("a second list with break")

for item in groceries:
    if item == "spam":
        break
    print(item)


item_to_find = input("What item")

found_at = None

for index in range(len(groceries)):
    if groceries[index] == item_to_find:
        found_at = index
        print("{0} found at position {1}".format(item_to_find,found_at))
        break