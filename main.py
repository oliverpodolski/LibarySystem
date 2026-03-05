import json
import os
from dataclasses import dataclass
from json import JSONDecodeError
from turtledemo.clock import datum

file_path = "data.json"


def create_file():
    with open(file_path, "w") as file:
        json.dump([], file, indent=4)
        print("File was created")
        main_menu()

def add_book(book, release_year, author):
    if not os.path.exists(file_path):
        create_file()
        return
    with open(file=file_path, mode="r") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            data = []
        biggest_number_id = 0
        for i in range(len(data)):
            value = data[i]["ID"]
            if value < biggest_number_id:
                pass
            else:
                biggest_number_id = value
        new_book = {
            "Book": book,
            "ID": biggest_number_id + 1,
            "Release Year": release_year,
            "Author": author
        }
        data.append(new_book)

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
            data = []
        if not data:
            print("There are no books saved in the file")
            return main_menu()
        for i in range(len(data)):
            print(f"{i}. Book: {data[i]['Book']} Author: {data[i]['Author']} Release Year: {data[i]['Release Year']} ID: {data[i]['ID']}")
    main_menu()

def delete_book(remove_book_id):
    if not os.path.exists(file_path):
        print("No File was found")
        create_file()
        return
    with open(file_path, "r") as file:
        found_book = False
        try:
            data = json.load(file)
        except JSONDecodeError:
            data = []
        if not data:
            print("There are no books saved in the File")
        for i in range(len(data)):
            if int(data[i]["ID"]) == int(remove_book_id):
                print(f"The book: {data[i]['Book']} was deleted!")
                del data[i]
                gefunden = True
                break
        if found_book != True:
            print(f"There is no book with the ID: {remove_book_id}!")

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
    main_menu()

def search_for_book(input_text):
    input_text = input_text.lower()
    found_books = 0
    if not os.path.exists(file_path):
        print("No file was found")
        create_file()
        return
    with open(file_path, "r") as file:
        try:
            data = json.load(file)
        except JSONDecodeError:
            print("There are no books in the file saved!")#
            return main_menu()
        for i in range(len(data)):
            book_name = data[i]["Book"]
            book_author = data[i]["Author"]
            if input_text in book_name.lower() or input_text in book_author.lower():
                print(f"{i}. Book: {data[i]['Book']} Author: {data[i]['Author']} Release Year: {data[i]['Release Year']} ID: {data[i]['ID']}")
                found_books += 1
        if found_books == 0:
            print(f"There was no book or author found with the name: {input_text}")
        main_menu()

def main_menu():
    main_menu_option = int(input("\nWhat would you like to do?\n1. ADD A BOOK\n2. READ BOOK LIST\n3. REMOVE A BOOK\n4. SEARCH FOR A BOOK\n"))
    if main_menu_option == 1:
        get_name = input("Enter the name of the Book: ")
        get_release_year = int(input("Enter the release year: "))
        get_author = input("Enter the Author: ")
        add_book(get_name,get_release_year,get_author)
    elif main_menu_option == 2:
        read_books()
    elif main_menu_option == 3:
        get_remove_book_id = int(input("Enter the Book_ID:"))
        delete_book(get_remove_book_id)
    elif main_menu_option == 4:
        get_search_text = input("Enter the name of the book or the author you are looking for:\n")
        search_for_book(get_search_text)
    else:
        print("Enter a valid choice!")


main_menu()