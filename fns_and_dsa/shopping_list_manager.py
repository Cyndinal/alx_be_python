# Question
# Utilize Python lists to create a simple
# shopping list manager that allows users to add items,
# view the current list, and remove items.

# user interface
def display_menu():
    print("Shopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View all items")
    print("4. Exit")


def shopping_list_menu():
    # global add_item
    shopping_list=[]
    while True:
        display_menu()
        options= int(input("\nEnter the item to add:\n"))

        match options:
            case 1:
                add_item = input("Enter name of item: ")
                shopping_list.append(add_item)
            case 2:
                remove_item = input("Enter name of item to remove: ")
                if not remove_item in shopping_list:
                    print(f"{remove_item} Item not found!!")
                else:
                    print(f"{remove_item} Item removed!!")
                    shopping_list.remove(remove_item)
            case 3:
                for item,index in enumerate(shopping_list,start=1):
                    print(f"{item}-->{index}")
            case 4:
                exit(0)
            case _:
                print("\nInvalid choice!!\nTry again!!\n")


shopping_list_menu()