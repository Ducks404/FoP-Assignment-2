

# Prompts user to select an event
def selectEvent():
    pass

# Register a new event
def registerEvent():
    pass

# Update existing event
def updateEvent():
    pass

# Delete existing event
def deleteEvent():
    pass

# Manage attendees menu
def manageAttendees():
    pass

# Prints event schedule:
def printSchedule():
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
        registerEvent()
    elif choice == '2':
        updateEvent()
    elif choice == '3':
        deleteEvent()
    elif choice == '4':
        manageAttendees()
    elif choice == '5':
        printSchedule()
    elif choice =='6':
        break
    else:
        print('Error: Invalid choice')