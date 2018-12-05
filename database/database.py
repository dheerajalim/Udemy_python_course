import sqlite3


def establish_connection(db):
    connection = sqlite3.connect(db)
    cursor = connection.cursor()

    return cursor,connection


def create_table():

    conn = establish_connection("data.db")

    conn[0].execute("CREATE table if not exists books(name text primary key,author text,read integer)")

    conn[1].commit()
    conn[1].close()


def add_new_book(name,author):
    try:
        create_table()
        conn = establish_connection("data.db")
        conn[0].execute("Insert into books values(? , ? , 0)", (name, author))

        conn[1].commit()
        conn[1].close()

    except Exception as e:
        print(e)


def list_all_books():

    try:
        conn = establish_connection("data.db")
        conn[0].execute("Select * from books")

        book_list = [[data[0] , data[1], data[2]] for data in conn[0].fetchall()]

        conn[1].close()

        return book_list

    except Exception as e:
        print(e)


def mark_read_book(search):

    try:
        conn = establish_connection("data.db")
        records = conn[0].execute("select * from books where name like ? or author like ?", ('%'+search+'%','%'+search+'%'))

        if not records.fetchall():
            print("No such record available to be updated")

        else:
            conn[0].execute("Update books set read = 1 where name like ? or author like ? ",
                                     ('%' + search + '%', '%' + search + '%'))
            conn[1].commit()
            conn[1].close()

            print("Data updated successfully")

    except sqlite3.ProgrammingError as e:
        print(e)


def delete_book(search):

    try:
        conn = establish_connection("data.db")

        records = conn[0].execute("select * from books where name = ?",
                                  (search,))

        if not records.fetchall():
            print("No such record available to be deleted")

        else:
            conn[0].execute("Delete from books where name = ?", (search,))
            conn[1].commit()
            conn[1].close()

            print("Data deleted successfully")

    except sqlite3.ProgrammingError as e:
        print(e)

