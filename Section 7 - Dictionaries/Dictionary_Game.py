#This game contains a procedurally created dungeon
#It will have two mechanics - dungeon creation and combat

# this represents the health of the player and will raise or lower based on combat
player_health = 10
current_locaton = 55

# this represents the created rooms and directions, for this exercise, we will use a grid system the dungeon is a 10x10 grid
# for now we'll store the room info in a dictionary, later we'll use an object
# the coordinates will be the key for the room and represent north(10) - south(1) and east(10) - west(1)
# the dungeon map represents the doors availalbe in a given room
known_rooms = {55:"1"}

dungeon_map = {55:("N","S","W","E")}

# room types is metadata used to describe the room when entered
room_types = {"1": "The room around you is stone with dripping water and bones scattered around the floor. Please choose a direction.",
              "2": "A torture chamber. A recent victim lies on the rack."
              }

# this function generates a new room
def room_generator(room_location, choice):
    #first determine if the room already exists in the dictonary
    #if not, determine if any adjacent rooms share a wall and if there is a door
    #if there is a door, add it
    #if there is no door, randomly determine whether to include a door
    #also determine the room type

    new_room_location = ""
    if choice == "N":
        new_room_location = room_location + 10
    elif choice == "S":
        new_room_location = room_location - 10
    elif choice == "W":
        new_room_location = room_location - 1
    else:
        new_room_location = room_location +1

    #for now hardcode a room
    known_rooms[new_room_location]="2"
    dungeon_map[new_room_location]=("N","S","W","E")
    print("new room {} added".format(new_room_location))
    return new_room_location

print("You have entered a dungeon and need to escape.")

while True:
    # tell them thier current health
    print("Your health is {}".format(player_health))

    # describe the room
    room_type = known_rooms[current_locaton]
    print("{}".format(room_types[room_type]))
    
    # list exits
    print("available exits are (press Q to quit):")
    for exit in dungeon_map[current_locaton]:
        print(exit)

    # prompt for choice
    choice = input()

    # create room and loop
    if(choice == "Q"):
        break
    else:
        new_room_loc = room_generator(current_locaton,choice)
        current_locaton = new_room_loc