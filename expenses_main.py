import pandas
import numpy
import matplotlib
import os
from os.path import exists
import sys
from datetime import datetime


quit_flag = False # Is set when the user quits.
home = os.path.expanduser('~') # Path for user home directory
expenses_db = os.path.join(home, '.expenses_db') # Path for expenses db
# Load existing db, or create a new one.
if exists(expenses_db):
    print("Loading expenses database . . .")
    db = pandas.read_csv(expenses_db)
else:
    print("No expenses database found. Would you like to load an existing database, or generate a new one?")
    valid_input = False
    while not valid_input:
        print("Insert n or leave empty for new database\nInsert l to load an already existing database")
        user_input = input()
        if user_input.lower() == 'l':
            print("Please provide the full path for the database.")
            path_to_db = input()
            if exists(path_to_db):
                print("Loading database . . .")
                db = pandas.read_csv(path_to_db)
                valid_input = True
            else:
                print("File not found! Please enter a correct path, or generate a new database")
        elif user_input == '' or user_input.lower() == 'n':
            print("Creating a new database . . .")
            db = pandas.DataFrame(columns=['ID','Day', 'Month', 'Year', 'Amount', 'Category', 'Description', 'Logging date'])
            valid_input = True
        else:
            print("Please insert a valid input!")
    print("Saving database . . .")
    db.to_csv(expenses_db, index=False)


# Gets a date from the user as an input.
def get_date():
    date_str = input("Insert the date of the transaction. Use the format of DD/MM/YYYY\n")
    valid_date = False
    while not valid_date:
        try:
            new_date = datetime.strptime(date_str, "%d/$m/$Y")
            valid_date = True
        except:
            print("The date does not match to the DD/MM/YYYY format. Please try again")
    return new_date

# Gets a new id
def get_new_id():
    return db['ID'].max()+1

def get_amount():
    pass

def insert_new_entry():
    new_date = get_date()
    new_id = get_new_id()




def delete_entry():
    pass

def monthly_summary():
    pass

def yearly_summary():
    pass

def category_summary():
    pass

while not quit_flag:
    categories = db['Category'].unique()
    user_input = input("[1] to insert a new entry\n[2] to delete an entry\n[3] for monthly summary\n[4] for yearly summary\n[5] for category summary (monthly)\n[q] to quit")
    if user_input == '1':
        insert_new_entry()
    elif user_input == '2':
        delete_entry()
    elif user_input == '3':
        monthly_summary()
    elif user_input == '4':
        yearly_summary()
    elif user_input == '5':
        category_summary()
    if user_input == "q":
        quit_flag = True
