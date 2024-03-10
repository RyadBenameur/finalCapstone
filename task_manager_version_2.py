""" Task 17 - Capstone Project"""
# Notes:
# 1. Use the following username and password to access the admin rights
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
import sys
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

def printing_task(counter,out_task):
    """Function to print out tasks in a readable format"""

    # Add all of the infomation into a single string, and print it out at the end
    disp_str = "\n\n\n#######################################################################\n"
    disp_str += f"{counter}.\n"
    disp_str += f"Task: \t\t {out_task['title']}\n"
    disp_str += f"Assigned to: \t {out_task['username']}\n"
    disp_str += f"Date Assigned: \t {out_task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
    disp_str += f"Due Date: \t {out_task['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
    disp_str += f"Task Completed?\t {"Yes" if out_task['completed'] is True else "No"}\n"
    disp_str += f"Task Description: \n {out_task['description']}\n"
    disp_str += "#######################################################################\n"
    print(disp_str)


def reg_user():
    """Add a new user to the user.txt file"""
    # Loop so user can retry if username has already been used, or is too short.
    username_validation = False
    while username_validation is False:
        new_username = input("New Username: ")
        if new_username in username_password:
            print("Username already used.")
        elif len(new_username) < 2 :
            print("Username is not valid!")
        else:
            print("Valid username")
            username_validation = True

    # Password loop is checked for length of password.
    password_validation = False
    while password_validation is False:
        new_password = input("New Password: ")
        if len(new_password) > 1:
            password_validation = True
        else:
            print("Invalid password!")

    # New password will be compared to confirmation, then added to dictionary.
    confirm_password = input("Confirm Password: ")
    if new_password == confirm_password :
        print("New User Added!")
        username_password[new_username] = new_password

        # Add the new password and username into the user.txt file
        with open("user.txt", "w",encoding="utf-8") as out_file:
            user_data = []
            for k, passw in username_password.items():
                user_data.append(f"{k};{passw}")
            out_file.write("\n".join(user_data))

    else:
        print("Passwords do not match!")


def add_task():
    """Allow a user to add a new task to task.txt file"""
    # Prompt a user for the following:
    # A username of the person whom the task is assigned to,
    # A title of a task,
    # A description of the task and
    # the due date of the task.

    # Loop to ensure username is within the username_password dictionary
    username_verified = False
    while username_verified is False:
        task_username = input("Name of person assigned to task: ")
        if task_username not in username_password:
            print("User does not exist. Please enter a valid username")
        else:
            username_verified = True

    # Insert Task Infomation, loop to ensure date is formatted correctly
    task_verification = False
    while task_verification is False:
        task_title = input("Title of Task: ")
        task_description = input("Description of Task: ")

        # Checking if task title and description is long enough
        if len(task_title) < 3 or len(task_description) < 3:
            print("Invalid Task Data")

        # Checking if task data is only numbers (possible logic error)
        elif task_title.isdigit() is True or task_description.isdigit() is True:
            print("Invalid Task Data")
        else:
            task_verification = True
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")


    # Then get the current date.
    curr_date = date.today()
    # Add the data to the file task.txt and
    # Include 'No' to indicate if the task is complete.

    # Create dictionary for task
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }


    task_list.append(new_task)
    with open("tasks.txt", "w",encoding="utf-8") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("Task successfully added.")


def view_all():
    '''Reads the task from task.txt file and prints to the console in the 
        format of Output 2 presented in the task pdf (i.e. includes spacing
        and labelling) 
    '''

    for t in task_list:
        disp_str = f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Completed?\t {"Yes" if t['completed'] is True else "No"}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)


def username_editor(e_task):
    """Loops until username that is in user.txt is input
        then rewrites task.txt with the changes made by user"""

    # Create a loop unti valid username is entered into the program.
    # Entering -1 exits the function, and returns None so no edit is made.
    username_verified = False
    while username_verified is False:
        new_username = input("Please Enter the new Username, or -1 to exit: ")
        if new_username == "-1":
            print("Cancelling edit")
            print("\n"*5)
            return None
        elif new_username not in username_password:
            print(f"{new_username} is not a valid username!")
        else:
            print("Accepted username. Editing now.")
            username_verified = True

    # Search the task_list for the current task, and change the value in the list.
    for t in task_list:
        if t == e_task:
            t["username"] = new_username

    # Rewrite in tasks.txt to save the change into the file.
    with open("tasks.txt", "w",encoding="utf-8") as task_edit:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_edit.write("\n".join(task_list_to_write))
    return None


def date_editor(e_task):
    """Loops until date that is valid is entered,
    then rewrites task.txt with change made by user"""

    # Creates a loop until a valid date is entered.
    date_verified = False
    while date_verified is False:

        # Use Try Except to ensure no errors from invalid data
        # If -1 is entered, Return None and end function with no changes
        try:
            new_date = input("New due date of task (YYYY-MM-DD) or -1 to cancel edit: ")
            if new_date == "-1":
                print("Cancelling Edit")
                print("\n"*5)
                return None

            new_date_time = datetime.strptime(new_date, DATETIME_STRING_FORMAT)
            if new_date_time > datetime(2025, 1, 1) or new_date_time < datetime.today():
                print("Date is outside of reasonable boundaries. Please Input a valid date")
            else:
                print("Valid Date. Editing now")
                date_verified = True
        except ValueError:
            print("Invalid datetime format. Please use the format specified")

    # Search the task_list for the current task, and change the value in the list.
    for t in task_list:
        if t == e_task:
            t["due_date"] =  new_date_time

    # Rewrite in tasks.txt to save the change into the file.
    with open("tasks.txt", "w", encoding="utf-8") as task_edit:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_edit.write("\n".join(task_list_to_write))
    return None


def completion_editor(e_task):
    """Loops until valid option is chosen,
        then rewrites task.txt with changes made by user"""

    # Creates a loop until a valid option is made, "y" or "n".
    # if user inputs -1, function returns None and no changes are made.
    completion_verifed = False
    while completion_verifed is False:
        new_complete = input("Is task complete? y/n, or enter -1 to exit: ").lower()
        if new_complete == "-1":
            print("Cancelling change")
            print("\n"*5)
            return None

        elif new_complete == "y":
            # Find the matching task dictionary, and edit the value
            for t in task_list:
                if t == e_task:
                    t["completed"] = True
            completion_verifed = True
        elif new_complete == "n":
            print("Task not Completed")
            completion_verifed = True
        else:
            print("Please enter a valid option!")

    # Rewrite tasks.txt to save the changes made.
    with open("tasks.txt", "w",encoding="utf-8") as task_edit:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_edit.write("\n".join(task_list_to_write))

    return None


def view_mine():
    '''Outputs all of the users current tasks,
        as well as giving the user the option to edit tasks
        that have not been completed.
    '''
    print("\n"*5)

    # Loop created to allow user to choose a task to edit, or to exit and return to main menu.
    # We will also reprint chosen task.
    user_editing = True
    while user_editing is True:

        # Generate list to insert all of current users tasks and
        # counter to display number next to list for user to choose task later.
        user_task_list = []
        user_task_counter = 0

        # Each item in the task list is checked to see if it is the users.
        # If they are, they are printed in a user-friendly format.
        for t in task_list:
            if t['username'] == curr_user:
                user_task_counter += 1
                user_task_list.append(t)
                printing_task(user_task_counter,t)

        # User enters a number to choose a task to edit, or -1 to exit this option.
        # If invalid option is entered, user is sent to main menu.
        try:
            user_task_choice = int(input("Please choose a task, or to exit, enter -1:"))
            if user_task_choice == -1:
                print("Exiting view my tasks!")
                print("\n"*5)
                break

            task_chosen = user_task_list[user_task_choice-1]
            printing_task(user_task_choice,task_chosen)

            # User is brought back to main menu if task is completed.
            # Loop is to ensure that the user chooses a valid option.
            while True:
                if task_chosen["completed"] is True:
                    print("Task cannot be edited as it has been marked as completed!")
                    print("\n"*5)
                    user_editing = False
                    break

                # The user chooses a way to edit the task.
                user_edit_choice = input("""Please select an option:
u - edit the username assigned
d - edit the date assigned
c - mark as completed
b - go back\n\nPlease Enter Choice: """).lower()

                # Function called for each. Brought back to task list once edit is complete.
                if user_edit_choice == "u":
                    username_editor(task_chosen)
                    print("\n"*5)
                    break

                elif user_edit_choice == "d":
                    date_editor(task_chosen)
                    print("\n"*5)
                    break

                elif user_edit_choice == "c":
                    completion_editor(task_chosen)
                    print("\n"*5)
                    break

                elif user_edit_choice == "b":
                    print("Going back to tasks!")
                    print("\n"*5)
                    break

                else:
                    print("Choice is not valid!\nTry Again!\n")

        except (IndexError, ValueError):
            print("Invalid option!\nReturning to main menu!")
            print("\n"*5)
            break


def gen_reports():
    "Function will generate two files, user_overview and task_overview for reporting"

    # Create list and dictionary to keep track of data with tasks
    total_task_report = 0
    task_report_dict = {
        "total_tasks" : 0,
        "complete_task" : 0,
        "incomplete_task" : 0,
        "overdue_task" : 0,
    }

    # Go through each task in "task_list", and increment data in dictionary that is relevant
    # Data : complete tasks, incomplete tasks, and overdue tasks (comparing to current date)
    for t in task_list:
        task_report_dict["total_tasks"] += 1
        total_task_report += 1
        if t["completed"] is True:
            task_report_dict["complete_task"] += 1
        else:
            task_report_dict["incomplete_task"] += 1
            if t["due_date"] < datetime.today():
                task_report_dict["overdue_task"] += 1

    # Create a file called task_overview, and create a list of the values from dictionary (t_attr)
    # List makes it easier to read the string formatting, as we have to do calculations
    # Then all data is overwritten into the file
    with open("task_overview.txt", "w",encoding="utf-8") as t_report:
        t_attr = [
            task_report_dict["total_tasks"],
            task_report_dict["complete_task"],
            task_report_dict["incomplete_task"],
            task_report_dict["overdue_task"]
        ]
        t_report.write("Task Report!\n\n")
        t_report.write(f"Total Number of Tasks: {t_attr[0]}\n")
        t_report.write(f"Total Number of Completed Tasks: {t_attr[1]}\n")
        t_report.write(f"Total Number of Uncompleted Tasks: {t_attr[2]}\n")
        t_report.write(f"Total Number of Overdue Tasks: {t_attr[3]}\n")
        t_report.write(f"Percentage of Incomplete Tasks: {t_attr[2]/t_attr[0]*100}%\n")
        t_report.write(f"Percentage of Overdue Tasks: {t_attr[3]/t_attr[0]*100}%\n")

    # User_reports_data will hold 1 dictionary on each user to iteration later
    # Total list index is determined by amount of users in dictionary username_password
    user_report_data = []
    total_users = 0
    for user in username_password:
        total_users += 1
        user_report_dict = {
            "username" : user,
            "total_tasks" : 0,
            "tasks_complete" : 0,
            "tasks_incomplete" : 0,
            "tasks_overdue" : 0
        }
        # Each item in the task_list is checked to match the username in focus
        # Dictionary is then incremented based on date matching dictionary keys

        for t in task_list:
            if t["username"] == user:
                user_report_dict["total_tasks"] += 1
                if t["completed"] is True:
                    user_report_dict["tasks_complete"] += 1
                else:
                    user_report_dict["tasks_incomplete"] += 1
                    if t["due_date"] < datetime.today():
                        user_report_dict["tasks_overdue"] += 1
        # Add new dictionary to list
        user_report_data.append(user_report_dict)

    # Create a file : user_overview -> write title and infomation -> loop on length of list
    # create a list of the values from dictionary from each loop (u_attr -> user attribute)
    # List makes it easier to read the string formatting, as we have to do calculations
    # Then all data is overwritten into the file

    print(total_task_report)

    with open("user_overview.txt", "w",encoding="utf-8") as u_report:
        u_report.write("User Report!\n\n")
        u_report.write(f"Total Amount of users: {total_users}\n")
        u_report.write(f"Total Number of Tasks: {t_attr[0]}\n\n")
        for user in user_report_data:
            u_attr = [
                user["username"],
                user["total_tasks"],
                user["tasks_complete"],
                user["tasks_incomplete"],
                user["tasks_overdue"]
            ]
            if u_attr[1] == 0:
                u_report.write(f"{u_attr[0]}:\n")
                u_report.write(f"Total Tasks: {u_attr[1]}\n\n")
            else:
                u_report.write(f"{u_attr[0]}:\n")
                u_report.write(f"Total Tasks: {u_attr[1]}\n")
                u_report.write(f"Percent of Tasks: {u_attr[1]/total_task_report*100}%\n")
                u_report.write(f"Percent of Completed Tasks: {u_attr[2]/u_attr[1]*100}%\n")
                u_report.write(f"Percent of Incomplete Tasks: {u_attr[3]/u_attr[1]*100}%\n")
                u_report.write(f"Percent of Overdue Tasks: {u_attr[4]/u_attr[1]*100}%\n\n")

    print("Report Generated!\n")


def display_stats():
    """Function will take the data straight from the tasks.txt file
        and user.txt file, and read the data to write down for the user"""

    # Open the task file as read, as we will output the read file first
    with open("tasks.txt","r",encoding="utf-8") as task_stat_r:

        # the list task_stats will hold each line from the tasks.txt file as an index.
        # Create a dictionary to hold final stats
        task_stats = task_stat_r.read().split("\n")
        task_stat_dict = {
            "complete_task" : 0,
            "incomplete_task" : 0,
            "overdue_task" : 0,
            "incomplete_percent" : 0,
            "overdue_percent" : 0
        }

        # Counting loop will go through each task, and update dictionary when conditions are met.
        # The enumerate function will add 1 to variable "count" each iteration.
        for count, t in enumerate(task_stats):
            task_component = t.split(";")
            if task_component[5] == "Yes":
                task_stat_dict["complete_task"] += 1
            else:
                task_stat_dict["incomplete_task"] += 1
                if datetime.strptime(task_component[3], DATETIME_STRING_FORMAT) < datetime.today():
                    task_stat_dict["overdue_task"] += 1


        # Increase count by 1 (as it starts with zero) and final calculations for task dictionary
        t_count = count + 1
        task_stat_dict["incomplete_percent"] = (task_stat_dict["incomplete_task"] / t_count) * 100
        task_stat_dict["overdue_percent"] = (task_stat_dict["overdue_task"] / t_count) * 100


    # Print out each line to represent final stats from dictionary.
    print("\n#############################################################\n")
    print("Task Stats!\n")
    print(f"Total Tasks: {t_count}")
    print(f"Total Number of Completed Tasks: {task_stat_dict["complete_task"]}")
    print(f"Total Number of Incomplete Tasks: {task_stat_dict["incomplete_task"]}")
    print(f"Total Number of Overdue Tasks: {task_stat_dict["overdue_task"]}")
    print(f"Percent of Incomplete Tasks : {task_stat_dict["incomplete_percent"]}")
    print(f"Percent of Overdue Tasks : {task_stat_dict["overdue_percent"]}")
    print("\n#############################################################\n\n")

    # Open the user.txt file to read.
    with open("user.txt","r",encoding="utf-8") as user_stat_r:

        # Create a list of the usernames in the file, to be iterated later.
        user_list = []
        for line in user_stat_r:
            user_list.append(line.split(";")[0])

        # Output the title for the User Statistics, and total users
        print("\n#############################################################\n")
        print("User Stats!\n")
        print(f"Total User Count : {len(user_list)}")


        # For each name in the list, we will create a fresh dictionary to output.
        for user_s in user_list:
            u_stat_dic = {
                "username" : user_s,
                "total_tasks" : 0,
                "tasks_complete" : 0,
                "tasks_incomplete" : 0,
                "tasks_overdue" : 0
            }

            # Go through each task in the task_stats list, and compare with the username.
            # If it matches the username, update values in the dictionary based on conditions met
            for t in task_stats:
                task_c = t.split(";")
                if task_c[0] == user_s:
                    u_stat_dic["total_tasks"] += 1
                    if task_c[5] == "Yes":
                        u_stat_dic["tasks_complete"] += 1
                    else:
                        u_stat_dic["tasks_incomplete"] += 1
                        if datetime.strptime(task_c[3], DATETIME_STRING_FORMAT) < datetime.today():
                            u_stat_dic["tasks_overdue"] += 1

            # We create a list of each value as we will be doing calculations.
            # This is done for sake of readability.
            u_attr = [
                u_stat_dic["username"],
                u_stat_dic["total_tasks"],
                u_stat_dic["tasks_complete"],
                u_stat_dic["tasks_incomplete"],
                u_stat_dic["tasks_overdue"]
            ]

            # If the user has no tasks on their name yet, no need to do calculations.
            # This also avoids dividing by zero errors.
            if u_attr[1] == 0:
                print(f"User: {u_stat_dic["username"]}")
                print(f"Total Tasks: {u_stat_dic["tasks_complete"]}\n")

            else:
                print(f"User: {u_stat_dic["username"]}")
                print(f"Total Tasks: {u_stat_dic["tasks_complete"]}")
                print(f"Percent of Tasks: {(u_stat_dic["total_tasks"] / t_count) * 100}%")
                print(f"Percent of Completed Tasks: {round(u_attr[2]/u_attr[1])*100}%")
                print(f"Percent of Incomplete Tasks: {round(u_attr[3]/u_attr[1])*100}%")
                print(f"Percent of Overdue Tasks: {round(u_attr[4]/u_attr[1])*100}%\n")
    print("\n#############################################################\n")




# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w",encoding="utf-8") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r',encoding="utf-8") as user_file:
    user_data = user_file.read().split("\n")
# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password


# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w",encoding="utf-8") as default_file:
        pass

with open("tasks.txt", 'r',encoding="utf-8") as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]

# Creates a list for tasks to be stored in as dictionaries
task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)

#====Login Section====
# This code reads usernames and password from the user.txt file to
# allow a user to login.

LOGGED_IN = False
while not LOGGED_IN:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password:
        print("User does not exist")

    elif username_password[curr_user] != curr_pass:
        print("Wrong password")

    else:
        print("Login Successful!")
        LOGGED_IN = True

while True:
    # Presenting the menu to the user.
    # Making sure that the user input is converted to lower case.
    menu = input('''
Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - generate reports
ds - Display statistics
e - Exit
: ''').lower()

    if menu == 'r':
        reg_user()
    elif menu == 'a':
        add_task()
    elif menu == 'va':
        view_all()
    elif menu == 'vm':
        view_mine()
    elif menu == "gr":
        gen_reports()
    elif menu == "ds":
        display_stats()
    elif menu == 'e':
        print('Goodbye!!!')
        sys.exit()
    else:
        print("You have made a wrong choice, Please Try again")

