
movie_collection = []


def menu():

    print("1. Add Movie \n 2. View Movie \n 3. Find Movie \n 4. Quit")
    user_choice = input("Enter your choice: ")
    return user_choice


def search_menu():

    search_para = input("Please enter one search parameter :"
                        " \n 1. Movie name \n 2. Actor \n 3. Year \n 4. Director \n ")

    return search_para


def add_movie():

    print("Please enter the details to add the movie to collection")

    movie_name = input("Movie Name")
    movie_actor = input("Actor")
    movie_year = input("Year")
    movie_director = input("Director")

    movie_details = {

        "movie_name" : movie_name,
        "movie_actor" : movie_actor,
        "movie_year" : movie_year,
        "movie_director" : movie_director
    }

    movie_collection.append(movie_details)

    return movie_collection


def view_movie():

    print("Please find the list of movies in collection")
    for i in range(0,len(movie_collection)):

        print("\n", movie_collection[i] ,"\n")


def search_movie(user_search_para,user_search_keyword):
    flag = 0
    for i in range(0,len(movie_collection)):

        if movie_collection[i][user_search_para].lower() == user_search_keyword.lower():
            print(movie_collection[i], "\n")
            flag = 1

    if flag == 0:
            print ("No result(s) found")


user_selection = menu()

while user_selection != '4':

    if user_selection == '1':
        add_movie()
        print("Movie added to collection!")
        user_selection = menu()

    elif user_selection == '2':

        if not movie_collection:
            print("Collection is empty , please retry \n")
            user_selection = menu()
            continue

        view_movie()
        user_selection = menu()

    elif user_selection == '3':

        if not movie_collection:
            print("Collection is empty , please retry \n")
            user_selection = menu()
            continue

        user_search_para = search_menu()

        if user_search_para.lower() == "movie name":
            user_search_para = "movie_name"

        elif user_search_para.lower() == "actor":
            user_search_para = "movie_name"

        elif user_search_para.lower() == "year":
            user_search_para = "movie_year"

        elif user_search_para.lower() == "director":
            user_search_para = "movie_director"

        else:
            print("Invalid Entry, retry")
            user_selection = '3'
            continue

        user_search_keyword = input(f"Enter the {user_search_para} value :  ")
        search_movie(user_search_para,user_search_keyword)
        user_selection = menu()

    else:
        print("Invalid Entry, retry")
        user_selection = menu()


else:
    print("Thanks for using movie collection tool")
