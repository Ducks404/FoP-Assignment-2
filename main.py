

# Prompts user to select an event
def selectEvent(database):
    nam=input('What is the name of the event?')
    for sub_list in database:
        if nam in sub_list:
            y= database.index(sub_list)
            return y
    print("Event not found!!!")
    


# Register a new event
def registerEvent(database):
    return database

# Update existing event
def updateEvent(database):
    pass

# Delete existing event
def deleteEvent(database):
    printSchedule(database)
    delegroup= selectEvent(database)
    del database[delegroup]
    print("Event succcessfully deleted :)")
    return database

# Manage attendees menu
def manageAttendees(database):
    pass

# Prints event schedule:
def printSchedule(database):
    print(database)
    pass




while True:
    # Read data from database
    database = []
    with open('database.txt', 'r') as file:
        content = file.readlines()
    for event in content:
        event = event.strip('\n')
        event = event.split(', ')
        event = event[:6] + [event[6:]]
        database.append(event)
    
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
        database = registerEvent(database)
    elif choice == '2':
        database = updateEvent(database)
    elif choice == '3':
        database = deleteEvent(database)
    elif choice == '4':
        database = manageAttendees(database)
    elif choice == '5':
        printSchedule(database)
    elif choice =='6':
        break
    else:
        print('Error: Invalid choice')

    # Testing the database
    # database = [database[0]]

    # Converts to format of database
    databaseString = ''
    for event in database:
        eventString = ''
        for item in event[:-1]:
            eventString += item + ', '
        attendees = event[-1]
        for person in attendees:
            eventString += person + ', '
        eventString = eventString.strip(', ') + '\n'

        databaseString += eventString

    # Writes to database
    with open('database.txt','w') as file:
        file.write(databaseString)