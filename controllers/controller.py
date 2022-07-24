
from crypt import methods
from turtle import title
from flask import render_template, request, redirect
from app import app
from models.book import Book
from models.library import *


@app.route('/')
def index():
    return "Home page"

@app.route('/library')
def library():
    return render_template('index.html', title="Home", library_list=library_list)

@app.route('/library/<index>')
def show_single_book(index):
    for book in library_list:
        if index == book.title:
            break
    return render_template('book.html', title="individual book", library_book=book)

@app.route('/add_book')
def add_new_book():
    return render_template('add_book.html', title = "add_a_book")

@app.route('/library/add_book', methods=['POST'])
def add_the_new_book_to_library():
    title = request.form["title"]
    author = request.form["author"]
    genre = request.form["genre"]
    new_book = Book(title, author, genre)
    add_book(new_book)
    return redirect('/library')

@app.route('/remove_book')
def remove_a_book():
    return render_template('remove_book.html', title = "remove a book")

@app.route('/library/remove_book', methods=['POST'])
def remove_a_book_from_library():
    render_template('remove_book.html', title = "remove a book")
    book_to_remove = request.form['title']
    remove_book(book_to_remove)
    return redirect('/library')

@app.route('/library/check_out/<index>')
def check_out(index):
    check_out_book(index)
    return redirect('/library/<index>')

@app.route('/library/check_in/<index>')
def check_in(index):
    check_in_book(index)
    return redirect('/library/<index>')   


