import mysql.connector

# Establish the connection
mydb = mysql.connector.connect(
  host="your_host",
  user="your_username",
  password="your_password",
  database="your_database"
)

# Create a cursor object
mycursor = mydb.cursor()


import tkinter as tk
from tkinter import messagebox
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create users table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    email TEXT UNIQUE,
    phone TEXT UNIQUE,
    password TEXT NOT NULL
)
''')
conn.commit()

# Function to handle user signup
def signup():
    email = email_entry.get()
    phone = phone_entry.get()
    password = password_entry.get()
    try:
        cursor.execute("INSERT INTO users (email, phone, password) VALUES (?, ?, ?)", (email, phone, password))
        conn.commit()
        messagebox.showinfo("Success", "Signup successful!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Email or phone number already exists")

# Function to handle user login
def login():
    email = email_entry.get()
    phone = phone_entry.get()
    password = password_entry.get()
    cursor.execute("SELECT * FROM users WHERE (email = ? OR phone = ?) AND password = ?", (email, phone, password))
    user = cursor.fetchone()
    if user:
        messagebox.showinfo("Success", "Login successful!")
        main_app()
    else:
        messagebox.showerror("Error", "Invalid email/phone or password")

# Function to show the main app after login
def main_app():
    login_frame.pack_forget()
    main_frame.pack()

# Set up the main window
root = tk.Tk()
root.title("Personal Expense Tracker")

# Create login/signup frame
login_frame = tk.Frame(root)
login_frame.pack()

tk.Label(login_frame, text="Email:").grid(row=0, column=0)
email_entry = tk.Entry(login_frame)
email_entry.grid(row=0, column=1)

tk.Label(login_frame, text="Phone:").grid(row=1, column=0)
phone_entry = tk.Entry(login_frame)
phone_entry.grid(row=1, column=1)

tk.Label(login_frame, text="Password:").grid(row=2, column=0)
password_entry = tk.Entry(login_frame, show='*')
password_entry.grid(row=2, column=1)

tk.Button(login_frame, text="Login", command=login).grid(row=3, column=0, columnspan=2)
tk.Button(login_frame, text="Signup", command=signup).grid(row=4, column=0, columnspan=2)

# Create main app frame
main_frame = tk.Frame(root)

tk.Label(main_frame, text="Amount:").grid(row=0, column=0)
amount_entry = tk.Entry(main_frame)
amount_entry.grid(row=0, column=1)

tk.Label(main_frame, text="Category:").grid(row=1, column=0)
category_entry = tk.Entry(main_frame)
category_entry.grid(row=1, column=1)

tk.Label(main_frame, text="Date:").grid(row=2, column=0)
date_entry = tk.Entry(main_frame)
date_entry.grid(row=2, column=1)

tk.Button(main_frame, text="Add Expense", command=add_expense).grid(row=3, column=0, columnspan=2)
tk.Button(main_frame, text="View Expenses", command=view_expenses).grid(row=4, column=0, columnspan=2)
tk.Button(main_frame, text="Total Expenses", command=total_expenses).grid(row=5, column=0, columnspan=2)

expenses_text = tk.Text(main_frame, height=10, width=50)
expenses_text.grid(row=6, column=0, columnspan=2)

total_label = tk.Label(main_frame, text="Total Expenses: 0")
total_label.grid(row=7, column=0, columnspan=2)

# Function to add an expense
def add_expense():
    amount = float(amount_entry.get())
    category = category_entry.get()
    date = date_entry.get()
    expense = {'amount': amount, 'category': category, 'date': date}
    expenses.append(expense)
    messagebox.showinfo("Info", "Expense added successfully!")
    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)

# Function to view all expenses
def view_expenses():
    expenses_text.delete(1.0, tk.END)
    for expense in expenses:
        expenses_text.insert(tk.END, f"Amount: {expense['amount']}, Category: {expense['category']}, Date: {expense['date']}\n")

# Function to calculate total expenses
def total_expenses():
    total = sum(expense['amount'] for expense in expenses)
    total_label.config(text=f"Total Expenses: {total}")

# Run the application
root.mainloop()
