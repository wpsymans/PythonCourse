class_list = ["Algebra","Geometry","English"]

student_name = input("Please enter your name.")

exit_prompt = 1

while exit_prompt == 1:
    list_choice = input("Would you like to see a list of classes? Y/N")
    if(list_choice == "Y"):
        for item in class_list:
            print("{} - ".format(class_list.index(item)) + item) 
            exit_prompt = 0
        

