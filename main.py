

# Prompts user to select an event
def selectEvent(database):
    pass

# Register a new event
def registerEvent(database):
    pass

# Update existing event
def updateEvent(database):
    pass

# Delete existing event
def deleteEvent(database):
    pass

# Manage attendees menu
def manageAttendees(database):
    pass

# Prints event schedule:
def printSchedule(database):
    pass

while True:
    print('''
        Event Management System
                Menu
    1. Register new event
    2. Update an existing event
    3. Delete an existing event
    4. Manage attendees for an existing event
    5. Print event schedule
    6. Exit''')
    choice = input('Enter choice: ')
    if choice == '1':
        registerEvent(database)
    elif choice == '2':
        updateEvent(database)
    elif choice == '3':
        deleteEvent(database)
    elif choice == '4':
        manageAttendees(database)
    elif choice == '5':
        printSchedule(database)
    elif choice =='6':
        break
    else:
        print('Error: Invalid choice')