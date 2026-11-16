my_list = []
previous_list = None
todo_list = []
completed_list = []

while True:
    print("Welcome your list!")
    print("\n1. Add an item")
    print("2. Remove an item")
    print("3. Display list")
    print("4. Undo previous change")
    print("5. Exit")

    choice = input("\nEnter your choice:")

    if choice == "1":
        print("Add an item selected")
        previous_list = my_list.copy()
        items = input("Enter items separated by commas: ").split(",")

        for item in items:
            my_list.append(item.strip())

        print("Items added!")

    elif choice == "2":
        print("Remove an item selected")
        for i in range(len(my_list)):
            print(i, my_list[i])
        index = int(input("Enter the index to remove: "))
        previous_list = my_list.copy()
        my_list.pop(index)
        print("Item removed!")

    elif choice == "3":
        print("Your current list:")
        for item in my_list:
            print(item)

    elif choice == "4":
        print("Undo previous change")
        if previous_list is not None:
            my_list = previous_list.copy()
            print("Previous change undone!")
        else:
            print("Nothing to undo!")
    elif choice == "5":
        print("Exiting program")
        break
    else:
        print("Invalid choice. Please try again")

