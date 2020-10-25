'''
Katie Sipos
10/24/2020
Python 1 - DAT-119 
Homework - midterm 
A todo list program that let's a user add, remove and view their list 
'''

# TODOS:
# if they enter a string use isnumeric = false before you assign cast to int


def add_to_list(todo_list):
    ''' a function that gets a task from a user and adds it to their todo list'''
    # get task from user and store in variable
    task = input('What is your task? ')
    # checks if task is empty and prompts user again if they just hit enter
    if len(task) == 0:
        task = input('You did not type anything! Enter text for your task: ')
    # append task to the todo list
    todo_list.append(task)


def view_list(printable_list):
    ''' this is a function that takes a generic list and formats it to print'''
    # start number at -1 so it works with proper indices
    number = 0
    # if the list has nothing in it, but they choose the option let them know they don't have anything on the list
    if len(printable_list) == 0:
        print('\nYou do not have anything on your list!')
    print('\n\nYour list items are:\n')
    # for loop that prints a pretty list
    for item in printable_list:
        number += 1
        print(number, ': ', item, sep=' ')


def remove_from_list(todo_list, completed_list):
    ''' a funtion that asks a user what they want to remove, removes that from the current todo list, and adds it to a completed list'''
    # print list for user
    view_list(todo_list)
    # ask the user what they want to remove
    user_choice = int(input('\nWhat number would you like to remove? '))
    # subtract 1 so that i can print user friendly numbers
    user_choice = user_choice - 1
    # assign item to the user choice (minus 1)
    item = todo_list[user_choice]
    # remove that item from the todo list
    todo_list.remove(item)
    # add item to completed list
    completed_list.append(item)


def quit_program():
    ''' a function that quits the program and does not persist the list'''
    print('\nGoodbye! Thank you for using the Todo List Application!')


def main():
    print('Welcome the Todo List Application!\n')
    # create all variables for program for current list, completed list, and the user's choice
    todo_list = []
    completed_list = []
    user_choice = 0
    # loop through program options as long as the user hasn't chosen 5
    while user_choice != 5:
        print('''
        Please choose one of the following options:\n 
        1. Add an item to your todo list\n
        2. View your current todo list\n 
        3. Mark an item as completed\n 
        4. View your completed list\n   
        5. Quit program (NOTE: your list will not be saved)\n 
        ''')
        # get user choice and decide what part of the program to run
        user_choice = int(input('What would you like to do? '))
        if user_choice == 1:
            add_to_list(todo_list)
        if user_choice == 2:
            view_list(todo_list)
        if user_choice == 3:
            remove_from_list(todo_list, completed_list)
        if user_choice == 4:
            view_list(completed_list)
    quit_program()


if __name__ == '__main__':
    main()
