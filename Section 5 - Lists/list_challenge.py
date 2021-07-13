#This program will support a number of functions invoked by a loop
#A default menu of available parts will be presented
#The user may add a new part or select and existing part
#If adding a new part, it will be available in the presentation menu
#If selecting a part, it will be added to the selected parts list
#Pressing check-out will exit the loop an present the selected parts

current_choice = "-"
selected_parts = "[]"
available_parts = ['Computer','Monitor','Keyboard']

while current_choice != "Checkout":
    print("Here is a list of available parts:")
    
#using enumerate to get the index position

    for number, available_part in enumerate(available_parts):
        print("{0} : {1}".format(number  + 1, available_part))
    
    print("You can select a part (a) or add a new part (b) or quit(Checkout)")
    menu_option = input()

    if menu_option == "a":
        print("Please enter a part number")
        current_choice = input()
        #look-up the part by index
        selected_parts += available_parts[int(current_choice)]
        continue

    if menu_option == "b":
        print("Enter a new part name")
        current_choice = input()
        available_parts += current_choice

    if menu_option == "Checkout":
        current_choice = "Checkout"

print(selected_parts)