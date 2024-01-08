
from flask import Flask, render_template, request, redirect, url_for,flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key' 

# Database initialization

def init_db():
    conn = sqlite3.connect('bulkybooks.db')
    cursor = conn.cursor()

    # Create bulkybooks table if not exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bulkybooks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            isbn TEXT NOT NULL,
            author TEXT NOT NULL,
            price INTEGER NOT NULL,
            category TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

# Initialize the database
init_db()

# Create
@app.route('/create', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        isbn = request.form['isbn']
        author = request.form['author']
        price = request.form['price']
        category = request.form['category']

        conn = sqlite3.connect('bulkybooks.db')
        cursor = conn.cursor()

        # Insert data into the bulkybooks table
        cursor.execute('INSERT INTO bulkybooks (title, description, isbn, author, price, category) VALUES (?, ?, ?, ?, ?, ?)',
                       (title, description, isbn, author, price, category))

        conn.commit()
        conn.close()

        flash('Book created successfully!', 'success')
        return redirect(url_for('get_books'))

    return render_template('create.html')

# Read
@app.route('/')
def get_books():
    conn = sqlite3.connect('bulkybooks.db')
    cursor = conn.cursor()

    # Fetch all books from the bulkybooks table
    cursor.execute('SELECT * FROM bulkybooks')
    bulkybooks = cursor.fetchall()

    conn.close()

    return render_template('index.html', bulkybooks=bulkybooks)

# Update
# Update
# Update
# Update
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def update(id):
    conn = sqlite3.connect('bulkybooks.db')
    cursor = conn.cursor()

    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        isbn = request.form['isbn']
        author = request.form['author']
        price = request.form['price']
        category = request.form['category']

        # Update data in the bulkybooks table
        cursor.execute('UPDATE bulkybooks SET title=?, description=?, isbn=?, author=?, price=?, category=? WHERE id=?',
                       (title, description, isbn, author, price, category, id))

        conn.commit()
        conn.close()

        flash('Employee updated successfully', 'success')
        return redirect(url_for('get_books'))  # Redirect to the book list page
    else:
        # Fetch the book data by id
        cursor.execute('SELECT * FROM bulkybooks WHERE id=?', (id,))
        bulkybooks = cursor.fetchone()

        conn.close()

        return render_template('update.html', bulkybooks=bulkybooks)


# Delete
@app.route('/delete/<int:id>')
def delete_book(id):
    conn = sqlite3.connect('bulkybooks.db')
    cursor = conn.cursor()

    # Delete the book by id
    cursor.execute('DELETE FROM bulkybooks WHERE id=?', (id,))

    conn.commit()
    conn.close()
    
    flash('Employee deleted successfully', 'success')
    return redirect(url_for('get_books'))

if __name__ == '__main__':
    app.run(debug=True)
