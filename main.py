from manager import LibraryManager
from items import Book, Magazine


def display_menu():
    print("\n 1. Add Book ")
    print("\n 2. Add Magazine")
    print("\n 3. View All Items")
    print("\n 4. Search Item by Title or Author")
    print("\n 5. Borrow Item")
    print("\n 6. Return Item")
    print("\n 7. Remove Item")
    print("\n 8. Exit")


def input_book():
    title = input(f"What is the name of the title? \n")
    author = input(f"What is the author name? \n")
    year = input(f"Which year It has been published? \n")
    genre = input(f"What is the Genre? \n")
    return Book(title=title, author=author, year=year, genre=genre)


def input_magazine():
    title = input(f"What is the name of the title \n")
    author = input(f"What is the author name \n")
    year = input(f"Which year It has been published \n")
    issue_number = input(f"What is the issue number \n")
    return Magazine(title, author, year, issue_number)


def main():
    manager = LibraryManager()

    while True:
        display_menu()
        print("-" * 70)
        number = input(f"please select the option using number (1 to 8) \n")

        if number == "1":
            manager.add_item(input_book())

        elif number == "2":
            manager.add_item(input_magazine())
        elif number == "3":
            manager.view_all_items()
        elif number == "4":
            search_term = input(
                "Can get the tilte or author name you want to search to get books/magazine \n"
            ).lower()
            manager.search_item(query=search_term)
        elif number == "5":
            borrowing_title = input(
                f"Please give the title name you want to borrow \n"
            ).lower()
            manager.borrow_item(borrowing_title)
        elif number == "6":
            return_title = input(
                "Please give the title name you want to return \n"
            ).lower()
            manager.return_item(return_title)
        elif number == "7":
            remove_item = input(f"What is the item you want to remove \n").lower()
            manager.remove_item(remove_item)
        elif number == "8":
            print("Exiting... Goodbye!")
            break


if __name__ == "__main__":
    main()
