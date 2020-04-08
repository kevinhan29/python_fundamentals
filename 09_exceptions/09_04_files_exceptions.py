'''
In this exercise, you will practice both File I/O as well as using Exceptions
in a real-world scenario.

You have a folder containing three text files of books from Project Gutenberg:
- war_and_peace.txt
- pride_and_prejudice.txt
- crime_and_punishment.txt

1) Open war_and_peace.txt, read the whole file content and store it in a variable

2) Open crime_and_punishment.txt and overwrite the whole content with an empty string

3) Loop over all three files and print out only the first character each. Your program
    should NEVER terminate with a Traceback.

    a) Which Exception can you expect to encounter? Why?

    b) How do you catch it to avoid the program from terminating with a Traceback?


BONUS CHALLENGE: write a custom Exception that inherits from Exception and raise it if the
first 100 characters of any of the files contain the string "Prince".

'''
import os

class hasPrince(Exception):
    def __init__(self, book_title):
        self.book_title = book_title

with open("/Users/kevinhan/Documents/CodingNomads/labs/09_exceptions/books/war_and_peace.txt", "r") as fin:
    war_and_peace = fin.readlines()

with open("/Users/kevinhan/Documents/CodingNomads/labs/09_exceptions/books/crime_and_punishment.txt", "w") as fout:
    fout.write("")

books_folder = "/Users/kevinhan/Documents/CodingNomads/labs/09_exceptions/books"
for book in os.listdir(books_folder):
    book_path = books_folder + "/" + book
    with open(book_path, mode='r', encoding='utf-8-sig') as fin:
        temp_str = fin.read(100)           # used to store up to first 100 chars in each file
        #breakpoint()
        try:
            print(f"First char in {book} is {temp_str[0]}")        # prints out first char
        except IndexError:
            print(f"{book} is empty, there is no first char")
        except:
            print("Something else went wrong")

        # find if "Prince" exists in first 100 chars of any of the files
        try:
            if temp_str.find("Prince") != -1:
                raise (hasPrince(book))
        except hasPrince as e:
            print("BONUS!", e.book_title, "also has the word 'Prince' in the first 100 chars")
        except:
            print("Something else went wrong")
        finally:
            print("")
