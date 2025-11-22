#Bookstore Application using Flask and SQLAlchemy to manage a collection of books. Accessed at http://127.0.0.1:5000/
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create the Flask application instance
app = Flask(__name__)

# Configure SQLite database file for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'

# Initialize the SQLAlchemy extension
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(150), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(100), nullable=True)
    
    def __repr__(self):
        return f"<Book {self.book_name} by {self.author}>"
    
# Homepage route
@app.route('/')
def index():
    return "Welcome to the Book Library!"

# Add a new book 
@app.route('/add_book/<name>/<author>/<publisher>')
def add_book(name, author, publisher):
    new_book = Book(book_name=name, author=author, publisher=publisher)
    db.session.add(new_book)
    db.session.commit()
    return f"Added book: {new_book}"

# List all books http://127.0.0.1:5000/books
@app.route('/books')
def list_books():
    books = Book.query.all()
    output = []
    for book in books:
        book_info = f"Name: {book.book_name}, Author: {book.author}, Publisher: {book.publisher}"
        output.append(book_info)
    return {"books": output}

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    


    