import tkinter as tk
import sqlite3

# Create a SQLite database and table
conn = sqlite3.connect("address_book.db")
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS addresses (
        first_name TEXT,
        last_name TEXT,
        address TEXT
    )
''')
conn.commit()

def insert_record():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    address = address_entry.get()
    conn.execute("INSERT INTO addresses (first_name, last_name, address) VALUES (?, ?, ?)", (first_name, last_name, address))
    conn.commit()
    update_display()

def delete_record():
    conn.execute("DELETE FROM addresses WHERE first_name=?", (first_name_entry.get(),))
    conn.commit()
    update_display()

def update_display():
    data = conn.execute("SELECT * FROM addresses")
    data = data.fetchall()
    data_text.set(data)

# Create the main GUI window
root = tk.Tk()
root.title("Address Book")

# Create entry widgets and labels for input fields
first_name_label = tk.Label(root, text="First Name")
first_name_entry = tk.Entry(root)
last_name_label = tk.Label(root, text="Last Name")
last_name_entry = tk.Entry(root)
address_label = tk.Label(root, text="Address")
address_entry = tk.Entry(root)

# Create buttons for inserting and deleting data
insert_button = tk.Button(root, text="Insert Record", command=insert_record)
delete_button = tk.Button(root, text="Delete Record", command=delete_record)

# Create a label for displaying the data
data_text = tk.StringVar()
data_label = tk.Label(root, textvariable=data_text)

# Pack widgets into the window
first_name_label.pack()
first_name_entry.pack()
last_name_label.pack()
last_name_entry.pack()
address_label.pack()
address_entry.pack()
insert_button.pack()
delete_button.pack()
data_label.pack()

# Start the GUI main loop
root.mainloop()

# Close the database connection when the application is closed
conn.close()
