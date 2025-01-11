# shopping_list_manager.py

def display_menu():
    print("\nShopping List Manager")
    print("1. View shopping list")
    print("2. Add item to shopping list")
    print("3. Remove item from shopping list")
    print("4. Exit")

def view_shopping_list(shopping_list):
    if not shopping_list:
        print("\nYour shopping list is empty.")
    else:
        print("\nYour shopping list:")
        for index, item in enumerate(shopping_list, start=1):
            print(f"{index}. {item}")

def add_item(shopping_list):
    item = input("\nEnter the item to add: ")
    shopping_list.append(item)
    print(f"{item} has been added to your shopping list.")

def remove_item(shopping_list):
    view_shopping_list(shopping_list)
    if shopping_list:
        try:
            item_index = int(input("\nEnter the number of the item to remove: "))
            if 1 <= item_index <= len(shopping_list):
                removed_item = shopping_list.pop(item_index - 1)
                print(f"{removed_item} has been removed from your shopping list.")
            else:
                print("Invalid item number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("\nEnter your choice: ")

        if choice == '1':
            view_shopping_list(shopping_list)
        elif choice == '2':
            add_item(shopping_list)
        elif choice == '3':
            remove_item(shopping_list)
        elif choice == '4':
            print("Exiting Shopping List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
