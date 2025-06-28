class LibraryItem:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = True

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, Released: {self.year}, Availability: {'Yes' if self.available else 'No'}"

    def to_dict(self):
        return {
            "Title": self.title,
            "Author": self.author,
            "Released": self.year,
            "Availability": "Yes" if self.available else "No",
        }


class Book(LibraryItem):

    def __init__(self, title, author, year, genre):
        super().__init__(title, author, year)
        self.genre = genre

    def display_info(self):
        print("--------------Book----------------")
        print(f"Title       : {self.title}")
        print(f"Author      : {self.author}")
        print(f"Released    : {self.year}")
        print(f"Genre       : {self.genre}")
        print(f"Availability: {'Yes' if self.available else 'No'}")

    def to_dict(self):
        data = super().to_dict()
        data["genre"] = self.genre
        return data


class Magazine(LibraryItem):
    def __init__(self, title, author, year, issue_number):
        super().__init__(title, author, year)
        self.issue_number = issue_number

    def display_info(self):
        print("-----------Magazine-------------")
        print(f"Title        : {self.title}")
        print(f"Author       : {self.author}")
        print(f"Released     : {self.year}")
        print(f"Issue Number : {self.issue_number}")
        print(f"Availability : {'Yes' if self.available else 'No'}")

    def to_dict(self):
        data = super().to_dict()
        data["issue_number"] = self.issue_number
        return data
