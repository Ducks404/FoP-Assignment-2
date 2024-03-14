

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

    eventINDEX = selectEvent(database)
    loop = True
    while loop:
        print()
        print(f"Event Name       : {database[eventINDEX][0]}")
        print(f"Event Description: {database[eventINDEX][1]}")
        print(f"Event Location   : {database[eventINDEX][2]}")
        print(f"Event Date       : {database[eventINDEX][3]}")
        print(f"Event Time, START: {database[eventINDEX][4]}")
        print(f"             END : {database[eventINDEX][5]}")
        j = ", ".join(database[eventINDEX][6])
        print(f"Attendee(s)      : {j}")
        print()
        print("◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉")
        print("            Event Update")
        print("                Menu")
        print("    1. Event Name")
        print("    2. Event Description")
        print("    3. Event Location")
        print("    4. Event Date")
        print("    5. Event Time")
        print("    6. Event Attendee's Name")
        print("    7. Back to Main Menu")
        print("◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉")
        updateChoice = input("Enter choice: ")

        if updateChoice.isdigit():
            updateChoice = int(updateChoice)
            
            # 1. Event Name
            if updateChoice == 1:
                updateEventName = input("Enter a new event name: ")
                database[eventINDEX][0] = updateEventName
                print("Event Name updated!")

            # 2. Event Description    
            elif updateChoice == 2:
                updateEventDescription = input("Enter a new event description: ")
                database[eventINDEX][1] = updateEventDescription
                print("Event Description updated!")

            # 3. Event Location
            elif updateChoice == 3:
                updateEventLocation = input("Enter a new event location: ")
                database[eventINDEX][2] = updateEventLocation
                print("Event Location updated!")

            # 4. Event Date    
            elif updateChoice == 4:
                updateEventDate = input("Enter a new event date: ")
                database[eventINDEX][3] = updateEventDate
                print("Event Date updated!")

            # 5. Event Time
            elif updateChoice == 5:
                loop_Time = True
                while loop_Time:
                    print()
                    print("Which do you want to update?")
                    print(" 1. Start Time")
                    print(" 2. End Time")
                    print(" 3. Go back")
                    print()
                    timeChoice = input("Your choice: ")

                    if timeChoice.isdigit():
                        timeChoice = int(timeChoice)

                        # 1. Start Time
                        if timeChoice == 1:
                            updateEventStartTime = input("Enter a new event start time: ")
                            database[eventINDEX][4] = updateEventStartTime
                            print("Event Start Time updated!")
                            
                        # 2. End Time
                        elif timeChoice == 2:
                            updateEventEndTime = input("Enter a new event end time: ")
                            database[eventINDEX][5] = updateEventEndTime
                            print("Event End Time updated!")

                        # 3. Go back
                        elif timeChoice == 3:
                            loop_Time = False

                        else:
                            print("Please try again.")
                    
                    else:
                        print("Try again. Choose 1 or 2 only.")

            # 6. Event Attendee's Name
            elif updateChoice == 6:
                loop_AttendeeName = True
                while loop_AttendeeName:
                    number = 1
                    print()
                    print("Attendees List:")
                    for i in database[eventINDEX][6]:
                        print(f"    {number}. {i}")
                        number += 1
                    
                    print()
                    print("What do you want to do?")
                    print(" 1. Add Attendee")
                    print(" 2. Delete Attendee")
                    print(" 3. Change Attendee's Name")
                    print(" 4. Go back")
                    print()
                    updateEventAttendeeName =input("What to do?: ")

                    if updateEventAttendeeName.isdigit():
                        updateEventAttendeeName = int(updateEventAttendeeName)

                        # 1. Add Attendee
                        if updateEventAttendeeName == 1:
                            addName = input("Who to add? (ENTER NAME): ")
                            database[eventINDEX][6].append(addName)
                            print("Attendee Name added!")

                        # 2. Delete Attendee
                        elif updateEventAttendeeName == 2:
                            loop_deleteAttendee = True
                            while loop_deleteAttendee:
                                deleteName = input("Who do you wish to delete? (ENTER NUMBER): ")

                                if deleteName.isdigit():
                                    deleteName = int(deleteName)

                                    if deleteName <= 0:
                                        print("Try again.")

                                    elif deleteName <= len(database[eventINDEX][6]):

                                        # Confirmation
                                        loop_ConfirmProceed = True
                                        while loop_ConfirmProceed:
                                            print()
                                            confirmProceed = input("Are you sure? (Y or N) : ")
                                            confirmProceed = confirmProceed.upper()

                                            if confirmProceed == "Y":
                                                database[eventINDEX][6].pop(deleteName - 1)
                                                print("Attendee Name deleted!")
                                                loop_ConfirmProceed = False
                                            
                                            elif confirmProceed == "N":
                                                loop_ConfirmProceed = False

                                            else:
                                                print("Enter 'Y' or 'N' only. Try again.")

                                        loop_deleteAttendee = False

                                    else:
                                        print("Try again.")
                                    
                                else:
                                    print("Please try again.")

                        # 3. Change Attendee's Name
                        elif updateEventAttendeeName == 3:
                            changeName = input("Which Attendee do you wish to change? (ENTER NUMBER) : ")

                            if changeName.isdigit():
                                changeName = int(changeName)

                                if changeName <= 0:
                                    print("Try again.")
                                
                                elif changeName <= len(database[eventINDEX][6]):
                                    print()
                                    newlyChangedName = input(f"Change '{database[eventINDEX][6][changeName - 1]}' to? (ENTER NAME): ")
                                    database[eventINDEX][6][changeName - 1] = newlyChangedName
                                    print("Attendee Name changed!")

                                else:
                                    print("Try again.")
                        
                            else:
                                print("Numbers only. Try again.")

                            # 4. Go back
                        elif updateEventAttendeeName == 4:
                            loop_AttendeeName = False

                        else:
                            print("Invalid. Please try again.")

                    else:
                        print("Invalid options. Please try again.")

                print(database[eventINDEX])

            # 7. Back to Main Menu
            elif updateChoice == 7:
                print("Back to Main Menu......")
                loop = False
            
            else:
                print("Enter valid options only. Try again.")
        
        else:
            print("Please try again. Enter digits only.")

    return database

# Delete existing event
def deleteEvent(database):
    printSchedule(database)
    delegroup= selectEvent(database)
    del database[delegroup]
    print("Event succcessfully deleted :)")
    return database

# Manage attendees menu
def manageAttendees(database):
     eventIndex = selectEvent(database)
    attendees = database[eventIndex][6]

    while True:
        print("\nAttendee Management for:", database[eventIndex][0])
        print("1. Add Attendee")
        print("2. Remove Attendee")
        print("3. Search Attendees")
        print("4. Mark Attendance")
        print("5. Export Attendee List")
        print("6. Back to Main Menu")
        choice = input("Enter choice: ")

        # ... existing logic for choices 1, 2, and 6 ...

        if choice.isdigit():
            choice = int(choice)

            if choice == 3:
                searchAttendees(attendees.copy())  # Pass a copy to avoid modifying original list

            elif choice == 4:
                markAttendance(attendees)

            elif choice == 5:
                filename = input("Enter filename for export (e.g., attendees.csv): ")
                exportAttendees(attendees.copy(), filename)  # Pass a copy to avoid modifying original list

            else:
                print("Invalid choice. Please try again.")

        else:
            print("Invalid input. Please enter digits only.")

    database[eventIndex][6] = attendees
    return database

# Prints event schedule:
def printSchedule(database):
    event = database[selectEvent(database)]
    print('Name:',event[0])
    print('Description:',event[1])
    print('Location:',event [2])
    print('Date:',event[3])
    print('StartTime:',event[4])
    print('EndTime:',event[5])
    j = ", ".join(event[6])
    print('Attendee:',j)





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
