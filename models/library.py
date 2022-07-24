from models.book import *


book1 = Book("The Hobbit", "J.R.R. Tolkien", "Fantasy", False)
book2 = Book("The Bible", "Various", "Religious", False)

library_list = [book1, book2]

def add_book(new_book):
    library_list.append(new_book)

def remove_book(book_title):
    book_to_remove = None
    for book in library_list:
        if book_title == book.title:
            book_to_remove = book
            break
    library_list.remove(book_to_remove)


def check_out_book(book_to_check_out):
    for book in library_list:
        if book.title == book_to_check_out:
            book.checked_out = True
            break
    
def check_in_book(book_to_check_in):
    for book in library_list:
        if book.title == book_to_check_in:
            book.checked_out = False
            break