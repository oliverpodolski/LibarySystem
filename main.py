import json
import os
from json import JSONDecodeError

file_path = "data.json"


def create_file():
    with open(file_path, "w") as file:
        json.dump([], file, indent=4)
        print("File was created")
        main_menu

def add_book(book, book_id, release_year, author):
    if not os.path.exists(file_path):               # If there is no file a new file will get created
        create_file()
        return
    with open(file=file_path, mode="r") as file:
        try:                                    #If the file has nothing in it a new array
            data = json.load(file)              # gets created which will be added later to the json
        except json.JSONDecodeError:
            data = []
        new_book = {                            #New List with book information
            "Book": book,
            "ID": book_id,
            "Release Year": release_year,
            "Author": author
        }
        data.append(new_book)                   #The List gets appended to the array data

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
        print("Book was added!")
        main_menu()

def read_books():
    if not os.path.exists(file_path):
        print("No File was found")
        create_file()
        return
    with open(file_path, "r") as file:
        try:
            data = json.load(file)
        except JSONDecodeError:
            print("There are no books saved in the file or the file is broken")
            data = []
        if not data:
            print("There are no books saved in the file")
            return
        for i in range(len(data)):
            print(f"{i}. Book: {data[i]['Book']} Author: {data[i]['Author']} Release Year: {data[i]['Release Year']} ID: {data[i]['ID']}")
    main_menu()


def main_menu():
    main_menu_option = int(input("\nWhat would you like to do?\n1. ADD A BOOK\n2. READ BOOK LIST\n"))
    if main_menu_option == 1:
        get_name = input("Enter the name of the Book!")
        get_id = input("Enter the ID")
        get_release_year = int(input("Enter the release year!"))
        get_author = input("Enter the Author")
        add_book(get_name,get_id,get_release_year,get_author)
    elif main_menu_option == 2:
        read_books()
    else:
        print("Enter a valid choice!")


main_menu()