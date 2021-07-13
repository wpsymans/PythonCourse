from unpacking_tuple_in_loop import albums

while True:
    print("Please choose your album:")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}"
        .format(index +1, title))

    choice = input()

    if choice.isnumeric and 1 <= int(choice) <= len(albums):
        
        choice_as_int = int(choice) - 1

        # now get the album and display the songs

        print("Please choose from the available songs")

        for index, (position,title) in enumerate(albums[choice_as_int][3]):
            print("{}: {}".format(position, title))            

        song_choice = input()

        print("playing {}".format(albums[choice_as_int][3][int(song_choice)]))

    else:
        print("Invalid choice please try again.")
        continue