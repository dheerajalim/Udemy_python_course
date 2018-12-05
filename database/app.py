import database


class Books:

    def __init__(self):

        self.user_input = ""
        self.USER_CHOICE = """Enter:
        - 'a' to add new book
        - 'l' to list all books
        - 'r' to mar book as read
        - 'd' to delete book
        - 'q' to quit

        Your Choice:  """

        self.user_input = input(self.USER_CHOICE)
        self.name, self.author, self.search = "", "", ""

    def menu_navigation(self):
        self.user_input = input(self.USER_CHOICE)
        Books.menu(self)

    def menu(self):

        while self.user_input != 'q':

            if self.user_input.lower() == 'a':
                self.name = input("Enter book name: ")
                self.author = input("Enter author name: ")

                database.add_new_book(self.name, self.author)

            elif self.user_input.lower() == 'l':
                books = database.list_all_books()
                if not books:
                    print("No data available ")
                else:
                    for book in books:
                        read = 'YES' if book[2] else 'NO'
                        print(f'The book {book[0]} is writen by {book[1]} and the user read status is {read}')

            elif self.user_input.lower() == 'r':
                self.search = input("Please enter the book or author name to change book status to read: ")
                database.mark_read_book(self.search)

            elif self.user_input.lower() == 'd':
                self.search = input("Enter thr book name to delete: ")
                database.delete_book(self.search)

            else:
                print("Please enter correct value")

            Books.menu_navigation(self)


book_process = Books()

book_process.menu()




