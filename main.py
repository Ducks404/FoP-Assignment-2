import re

# Prompts user to select an event
def selectEvent(database):
    print()
    for index, event in enumerate(database):
        print(f'{index+1}. {event[0]}')
    nam=input('What is the name of the event?\n')
    print()
    for sub_list in database:
        if nam in sub_list:
            y= database.index(sub_list)
            return y
    print("Event not found!!!\n")
    
# Register a new event
def registerEvent(database):
    return database

# Update existing event
def updateEvent(database):

    eventINDEX = selectEvent(database)
    if eventINDEX == None:
        return database
    loop = True
    while loop:
        print()
        print("               Event")
        print("************************************")
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
        print("    6. Back to Main Menu")
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
                loop_Location = True
                while loop_Location:
                    updateEventLocation = input("Enter a new event location: ")

                    # To extract, then, copy pasta that one selected "eventINDEX"'s event into this 1st Temporary List (for comparison) and update it based on user input.
                    tempList = []
                    tempList.extend(database[eventINDEX])
                    tempList[2] = updateEventLocation

                    tempStartHour, tempStartMin = map(int, tempList[4].split(":"))
                    tempStart = tempStartHour*60 + tempStartMin
                    tempEndHour, tempEndMin = map(int, tempList[5].split(":"))
                    tempEnd = tempEndHour*60 + tempEndMin

                    # Copy Pasta everything in the database except the selected "eventINDEX"'s event into this 2nd Temporary List (for comparison).
                    compList = []
                    compList.extend(database)
                    del compList[eventINDEX]
                    
                    # Comparing 1st and 2nd Temporary List for clashing of Date, Location and Time all at once
                    clashFlag = False
                    for event in range(len(compList)):
                        compStartHour, compStartMin = map(int, compList[event][4].split(":"))
                        compStart = compStartHour*60 + compStartMin
                        compEndHour, compEndMin = map(int, compList[event][5].split(":"))
                        compEnd = compEndHour*60 + compEndMin
                        if tempList[2:4] == compList[event][2:4] and (((tempStart <= compEnd < tempEnd) or (tempStart < compStart <= tempEnd)) or (compStart <= (tempStart and tempEnd) <= compEnd)):
                            print("Clashing of Location, Date and Time with another existing event.")
                            print("Try again.")
                            tempList.clear()
                            compList.clear()
                            clashFlag = True
                            break
                    if not clashFlag:
                        tempList.clear()
                        compList.clear()
                        database[eventINDEX][2] = updateEventLocation
                        print(f"Event Location updated to '{updateEventLocation}' !")
                        loop_Location = False

            # 4. Event Date    
            elif updateChoice == 4:
                loop_Date = True
                while loop_Date:
                    updateEventDate = input("Enter a new date (DD/MM/YY): ")
                    match = re.match(r"^(0[1-9]|[1-2][0-9]|3[0-1])\/(0[1-9]|1[0-2])\/([0-9][0-9])$", updateEventDate)
                    if match:
                            
                        # To extract, then, copy pasta that one selected "eventINDEX"'s event into this 1st Temporary List (for comparison) and update it based on user input.
                        tempList = []
                        tempList.extend(database[eventINDEX])
                        tempList[3] = match.group(0)

                        tempStartHour, tempStartMin = map(int, tempList[4].split(":"))
                        tempStart = tempStartHour*60 + tempStartMin
                        tempEndHour, tempEndMin = map(int, tempList[5].split(":"))
                        tempEnd = tempEndHour*60 + tempEndMin

                        # Copy Pasta everything in the database except the selected "eventINDEX"'s event into this 2nd Temporary List (for comparison).
                        compList = []
                        compList.extend(database)
                        del compList[eventINDEX]
                        
                        # Comparing 1st and 2nd Temporary List for clashing of Date, Location and Time all at once
                        clashFlag = False
                        for event in range(len(compList)):
                            compStartHour, compStartMin = map(int, compList[event][4].split(":"))
                            compStart = compStartHour*60 + compStartMin
                            compEndHour, compEndMin = map(int, compList[event][5].split(":"))
                            compEnd = compEndHour*60 + compEndMin
                            if tempList[2:4] == compList[event][2:4] and (((tempStart <= compEnd < tempEnd) or (tempStart < compStart <= tempEnd)) or (compStart <= (tempStart and tempEnd) <= compEnd)):
                                print("Clashing of Location, Date and Time with another existing event.")
                                print("Try again.")
                                tempList.clear()
                                compList.clear()
                                clashFlag = True
                                break
                        if not clashFlag:
                            database[eventINDEX][3] = match.group(0)
                            print(f"Event Date updated to '{match.group(0)}' !")
                            tempList.clear()
                            compList.clear()
                            loop_Date = False
                    else:
                        print("Invalid Date. Please use the format DD/MM/YY")

            # 5. Event Time
            elif updateChoice == 5:
                # To extract, then, copy pasta that one selected "eventINDEX"'s event into this 1st Temporary List (for comparison).
                tempList = []
                tempList.extend(database[eventINDEX])

                loop_Time = True
                while loop_Time:
                    print()
                    print("Which do you want to update?")
                    print(" 1. Start Time")
                    print(" 2. End Time")
                    print(" 3. Check Time and Go back")
                    print()
                    timeChoice = input("Your choice: ")

                    if timeChoice.isdigit():
                        timeChoice = int(timeChoice)

                        # 1. Start Time
                        if timeChoice == 1:
                            loop_StartTime = True
                            while loop_StartTime:
                                updateEventStartTime = input("Enter a new start time (HH:MM): ")
                                match_1 = re.match(r"^(0[0-9]|1[0-9]|2[0-3])\:([0-5][0-9])$", updateEventStartTime)
                                if match_1:

                                    # Update 1st Temporary List based on user input.
                                    tempList[4] = match_1.group(0)
                                    print(f"Event Start Time updated temporarily to '{match_1.group(0)}' for checking!")
                                    loop_StartTime = False

                                else:
                                    print("Invalid Time format. Please use the format HH:MM")
                            
                        # 2. End Time
                        elif timeChoice == 2:
                            loop_EndTime = True
                            while loop_EndTime:
                                updateEventEndTime = input("Enter a new end time (HH:MM): ")
                                match_2 = re.match(r"^(0[0-9]|1[0-9]|2[0-3])\:([0-5][0-9])$", updateEventEndTime)
                                if match_2:

                                    # Update 1st Temporary List based on user input.
                                    tempList[5] = match_2.group(0)
                                    print(f"Event End Time updated temporarily to '{match_2.group(0)}' for checking!")
                                    loop_EndTime = False

                                else:
                                    print("Invalid Time format. Please use the format HH:MM")

                        # 3. Go back
                        elif timeChoice == 3:
                            tempStartHour, tempStartMin = map(int, tempList[4].split(":"))
                            tempStart = tempStartHour*60 + tempStartMin
                            tempEndHour, tempEndMin = map(int, tempList[5].split(":"))
                            tempEnd = tempEndHour*60 + tempEndMin

                            # Copy Pasta everything in the database except the selected "eventINDEX"'s event into this 2nd Temporary List (for comparison).
                            compList = []
                            compList.extend(database)
                            del compList[eventINDEX]
                            
                            # Comparing 1st and 2nd Temporary List for clashing of Date, Location and Time all at once
                            clashFlag = False
                            for event in range(len(compList)):
                                compStartHour, compStartMin = map(int, compList[event][4].split(":"))
                                compStart = compStartHour*60 + compStartMin
                                compEndHour, compEndMin = map(int, compList[event][5].split(":"))
                                compEnd = compEndHour*60 + compEndMin
                                if tempList[2:4] == compList[event][2:4] and (((tempStart <= compEnd < tempEnd) or (tempStart < compStart <= tempEnd)) or (compStart <= (tempStart and tempEnd) <= compEnd) or (tempStart <= (compStart and compEnd) <= tempEnd)):
                                    print("Clashing of Location, Date and Time with another existing event.")
                                    print("Try again.")
                                    tempList.clear()
                                    compList.clear()
                                    clashFlag = True
                                    break
                            if not clashFlag:
                                database[eventINDEX][4] = tempList[4]
                                database[eventINDEX][5] = tempList[5]

                                print("Event Start and End Time updated successfully!")
                                tempList.clear()
                                compList.clear()

                            loop_Time = False

                        else:
                            print("Please try again.")
                    
                    else:
                        print("Try again. Choose 1, 2 or 3 only.")
                        
            # 6. Back to Main Menu
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
    delegroup= selectEvent(database)
    if delegroup == None:
        return
    del database[delegroup]
    print("Event succcessfully deleted :)")
    return database


import csv
#helper function for export,called later
def exportAttendees(attendees, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Attendee Name"])
        for attendee in attendees:
            writer.writerow([attendee])
    print("Attendee list exported successfully!")

#Marking attendees system  
#updated logic to test
def mark_attendance(attendees):
    """
    Marks attendance for attendees in a list.

    Args:
        attendees (list): A list of dictionaries containing attendee information.
            Each dictionary should have 'name' (string) and 'status' (string) keys.

    Returns:
        tuple: A tuple containing two elements:
            1. Updated attendees list (list): The original list with attendance statuses updated.
            2. Marked attendees list (list): A list of names of attendees whose attendance was marked.
    """

    if not attendees:
        print("There are no attendees in the list.")
        return attendees, []  # Return empty list for marked attendees

    print("List of Attendees:")
    for i, attendee in enumerate(attendees):
        status = 'Attended' if attendee['status'].upper() == 'Y' else 'Not Attended'
        print(f"{i+1}. {attendee['name']} ({status})")

    marked_attendees = []
    while True:
        name_to_mark = input("Enter attendee name to mark attendance (or 'q' to quit): ").strip()
        if name_to_mark.lower() == 'q':
            break

        for attendee in attendees:
            if attendee['name'].lower() == name_to_mark.lower():
                if attendee['status'].upper() != 'Y':
                    attendee['status'] = 'Y'
                    marked_attendees.append(attendee['name'])
                    print(f"Attendance for {attendee['name']} has been marked successfully!")
                else:
                    print(f"{attendee['name']} is already marked as attended.")
                break
        else:  # This else corresponds to the for loop
            print(f"Attendee '{name_to_mark}' not found. Please try again or enter 'q' to quit.")

    print("Updated List of Attendees:")
    for i, attendee in enumerate(attendees):
        status = 'Attended' if attendee['status'].upper() == 'Y' else 'Not Attended'
        print(f"{i+1}. {attendee['name']} ({status})")

    return attendees, marked_attendees
#helper function for search        
def searchAttendees(attendees):
    search_term = input("Enter attendee name to search: ")
    search_results = [attendee for attendee in attendees if search_term.lower() in attendee.lower()]

    if search_results:
        print("Search Results:")
        for i, attendee in enumerate(search_results):
            print(f"{i+1}. {attendee}")
    else:
        print("No attendees found matching the search term.")
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

        if choice.isdigit():
            choice = int(choice)

            # 1. Add Attendee
            if choice == 1:
                addName = input("Who to add? (ENTER NAME): ")
                attendees.append(addName)
                print("Attendee Name added!")

            # 2. Delete Attendee
            elif choice == 2:
                print()
                print("Attendees List:")
                for index, attendee in enumerate(attendees):
                    print(f"    {index+1}. {attendee}")
                loop_deleteAttendee = True
                while loop_deleteAttendee:
                    deleteName = input("Who do you wish to delete? (ENTER NUMBER): ")

                    if deleteName.isdigit():
                        deleteName = int(deleteName)

                        if deleteName <= 0:
                            print("Try again.")

                        elif deleteName <= len(attendees):

                            # Confirmation
                            loop_ConfirmProceed = True
                            while loop_ConfirmProceed:
                                print()
                                confirmProceed = input("Are you sure? (Y or N) : ")
                                confirmProceed = confirmProceed.upper()

                                if confirmProceed == "Y":
                                    attendees.pop(deleteName - 1)
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

            # 3. Search for an attendee
            elif choice == 3:
                searchAttendees(attendees.copy())  # Pass a copy to avoid modifying original list

            # 4. Mark attendees' attendance
            elif choice == 4:
                attendees = markAttendance(attendees)

            # 5. Export attendee into file
            elif choice == 5:
                filename = input("Enter filename for export (e.g., attendees.csv): ")
                exportAttendees(attendees.copy(), filename)  # Pass a copy to avoid modifying original list
            
            # 6. Go back
            elif choice == 6:
                break

            else:
                print("Invalid choice. Please try again.")

        else:
            print("Invalid input. Please enter digits only.")

     database[eventIndex][6] = attendees
     return database


# Prints event schedule:
def printEventDetails(database):
    eventIndex = selectEvent(database)
    if eventIndex == None:
        return
    event = database[eventIndex]
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
    5. Print event details
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
        printEventDetails(database)
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
