from items import Book, Magazine


class LibraryManager:

    def __init__(self):
        self.data_item = {
            "The Alchemist": Book("The Alchemist", "Paulo Coelho", 1988, "Fiction"),
            "Atomic Habits": Book("Atomic Habits", "James Clear", 2018, "Self-help"),
            "Sapiens": Book("Sapiens", "Yuval Noah Harari", 2011, "History"),
            "Python Crash Course": Book(
                "Python Crash Course", "Eric Matthes", 2015, "Programming"
            ),
            "Clean Code": Book(
                "Clean Code", "Robert C. Martin", 2008, "Software Engineering"
            ),
            "National Geographic": Magazine(
                "National Geographic", "Various", 2023, "1101"
            ),
            "TIME": Magazine("TIME", "Time Editors", 2022, "1102"),
            "The Economist": Magazine("The Economist", "Editorial Board", 2024, "1103"),
            "Forbes": Magazine("Forbes", "Forbes Staff", 2023, "1104"),
            "Wired": Magazine("Wired", "Condé Nast", 2024, "1105"),
        }
        # self.data_item = [
        #     Book("The Alchemist", "Paulo Coelho", 1988, "Fiction"),
        #     Book("Atomic Habits", "James Clear", 2018, "Self-help"),
        #     Book("Sapiens", "Yuval Noah Harari", 2011, "History"),
        #     Book("Python Crash Course", "Eric Matthes", 2015, "Programming"),
        #     Book("Clean Code", "Robert C. Martin", 2008, "Software Engineering"),
        #     Magazine("National Geographic", "Various", 2023, "1101"),
        #     Magazine("TIME", "Time Editors", 2022, "1102"),
        #     Magazine("The Economist", "Editorial Board", 2024, "1103"),
        #     Magazine("Forbes", "Forbes Staff", 2023, "1104"),
        #     Magazine("Wired", "Condé Nast", 2024, "1105"),
        # ]

    def add_item(self, item):
        if item.title in self.data_item:
            print("Item is already inside the Library. ")
            return
        self.data_item[item.title] = item
        print("Item had added successfully")

    def remove_item(self, title):
        title = title.strip().lower()
        for key in list(self.data_item.keys()):
            if key.lower() == title:
                del self.data_item[key]
                print("Item has removed successfully")
                return
        print("Item not found.")

    def borrow_item(self, title):
        title = title.strip().lower()
        for key in self.data_item:
            if key.lower() == title:
                item = self.data_item[key]
                try:
                    if not item.available:
                        raise ValueError("Item is Currently not available.")
                    item.available = False
                    print("Item is borrowed succesfully")
                except ValueError as ve:
                    print(ve)
                return

    def return_item(self, title):
        title = title.strip().lower()
        for key in self.data_item:
            if key.lower() == title:
                item = self.data_item[key]
                if not item.available:
                    item.available = True
                    print("Item Successfully returned.")
                else:
                    print("Item was not borrowed.")
                return
        print("Item not found in the library.")

    def search_item(self, query):
        search_item = False
        for item in self.data_item.values():
            if query.lower() in item.title.lower():
                item.display_info()
                search_item = True
                break
            elif query.lower() in item.author.lower():
                item.display_info()
                search_item = True
                break
        if not search_item:
            print("No matching items found. ")

    def view_all_items(self):
        for item in self.data_item.values():
            item.display_info()
