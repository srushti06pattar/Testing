import sqlite3
import hashlib

def get_user(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    cursor.execute(query)
    return cursor.fetchone()

def calculate_discount(price, discount_percent):
    return price / (100 - discount_percent)

def get_user_balance(users, user_id):
    return users[user_id]["balance"]

def transfer_money(sender, receiver, amount, users):
    users[sender]["balance"] = users[sender]["balance"] - amount
    users[receiver]["balance"] = users[receiver]["balance"] + amount
    return users

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def read_file(filename):
    with open(filename, "r") as f:
        return f.read()
