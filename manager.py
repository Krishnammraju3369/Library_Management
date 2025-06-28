from items import Book, Magazine


class LibraryManager:

    def __init__(self):
        self.data_item = [
            Book("The Alchemist", "Paulo Coelho", 1988, "Fiction"),
            Book("Atomic Habits", "James Clear", 2018, "Self-help"),
            Book("Sapiens", "Yuval Noah Harari", 2011, "History"),
            Book("Python Crash Course", "Eric Matthes", 2015, "Programming"),
            Book("Clean Code", "Robert C. Martin", 2008, "Software Engineering"),
            Magazine("National Geographic", "Various", 2023, "1101"),
            Magazine("TIME", "Time Editors", 2022, "1102"),
            Magazine("The Economist", "Editorial Board", 2024, "1103"),
            Magazine("Forbes", "Forbes Staff", 2023, "1104"),
            Magazine("Wired", "Condé Nast", 2024, "1105"),
        ]

    def add_item(self, item):
        for l in self.data_item:
            if l.title.lower() == item.title.lower():
                print("Item is already inside the Library")
                return
        self.data_item.append(item)
        print("added succesfully")

    def remove_item(self, title):
        for l in self.data_item:
            if l.title.lower() == title.lower():
                self.data_item.remove(l)
                print("Removed Successfully")
                return
        print("Item not found")

    def borrow_item(self, title):
        found = False
        for item in self.data_item:
            try:
                if item.title.lower() == title.lower():
                    found = True
                    if item.available:
                        item.available = False
                        print("Item borrowed successfully")

                        return
                    else:
                        raise ValueError("Item is currently not availabe.")
            except ValueError as ve:
                print(ve)
                return
        if not found:
            print("Item not found in the library.")

    def return_item(self, title):
        found = False
        for item in self.data_item:
            try:
                if item.title.lower() == title.lower():
                    found = True
                    if not item.available:
                        item.available = True
                        print("Item successfully returned")

                        return
                    else:
                        raise ValueError("Item was not borrowed.")

            except ValueError as ve:
                print(ve)
                return
        if not found:
            print("Item not found in the library.")

    def search_item(self, query):
        found = False
        for item in self.data_item:

            if query.lower() in item.title.lower():
                item.display_info()
                found = True
                break
            elif query.lower() in item.author.lower():
                item.display_info()
                found = True
                break
        if not found:
            print("No matching items found. ")

    def view_all_items(self):
        for l in self.data_item:
            l.display_info()
