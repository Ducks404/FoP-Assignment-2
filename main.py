import re

# Prompts user to select an event
def selectEvent(database):
    print()
    for index, event in enumerate(database):
        print(f'{index+1}. {event[0]}')
    nam=input('What is the name of the event?\n').lower()
    print()
    for sub_list in database:
        if nam == sub_list[0].lower():
            y= database.index(sub_list)
            return y
    print("Event not found!!!\n")
    input('Press Enter to continue...')

'''Function to Check for event clashing and Time format
Input:
    - event: list with event format to be compared
    - database: list of event-formatted lists to compare the list to
    
Output:
    - clashFlag: Boolean of clash or not'''
def checkEventTime(event, database):
    eventStartHour, eventStartMin = map(int, event[4].split(":"))
    eventStart = eventStartHour*60 + eventStartMin
    eventEndHour, eventEndMin = map(int, event[5].split(":"))
    eventEnd = eventEndHour*60 + eventEndMin
    
    # Comparing the two lists for clashing of Date, Location and Time all at once
    clashFlag = False
    for compEvent in database:
        compStartHour, compStartMin = map(int, compEvent[4].split(":"))
        compStart = compStartHour*60 + compStartMin
        compEndHour, compEndMin = map(int, compEvent[5].split(":"))
        compEnd = compEndHour*60 + compEndMin
        if event[2:4] == compEvent[2:4] and ((eventStart < compStart < eventEnd) or (compStart < eventStart < compEnd) or (eventStart == compStart)):
            clashFlag = True
            break
    if eventEnd <= eventStart:
        clashFlag = 'Invalid time'
    return clashFlag

# Register a new event
def registerEvent(database):
    while True:
        validName = True
        new_name = input("Enter event name: ")
        for event in database:
            if new_name.lower() == event[0].lower():
                print('Name already taken')
                validName = False
                break
        if validName:
            break

    new_description = input("Enter event description: ")
    new_location = input("Enter event location: ")

    while True:
        new_date = input("Enter the date (DD/MM/YY): ")
        match = re.match(r"^(0[1-9]|[1-2][0-9]|3[0-1])\/(0[1-9]|1[0-2])\/([0-9][0-9])$", new_date)
        if match:
            new_date = match.group(0)
            break
        else:
            print("Invalid Date. Please use the format DD/MM/YY")

    while True:
        new_start_time = input("Enter event start time in 24 hour format (HH:MM): ")
        match = re.match(r"^(0[0-9]|1[0-9]|2[0-3])\:([0-5][0-9])$", new_start_time)
        if match:
            new_start_time = match.group(0)
            break
        else:
            print("Invalid Time format. Please use the format HH:MM")

    while True:
        new_end_time = input("Enter event end time in 24 hour format (HH:MM): ")
        match = re.match(r"^(0[0-9]|1[0-9]|2[0-3])\:([0-5][0-9])$", new_end_time)
        if match:
            new_end_time = match.group(0)
            break
        else:
            print("Invalid Time format. Please use the format HH:MM")

    new_event = [new_name, new_description, new_location, new_date, new_start_time, new_end_time, []]

    clashFlag = checkEventTime(new_event, database)

    if clashFlag == 'Invalid time':
        print('Invalid. End time must come after start time.')
    elif clashFlag == True:
        print()
        print("Clashing of Location, Date and Time with another existing event.")
        print("Try again.")
    else:
        database.append(new_event)
        print("Event added!")
        print("Event:")
        print(f"\n\
Name       : {new_name}\n\
Description: {new_description}\n\
Location   : {new_location}\n\
Date       : {new_date}\n\
Start Time : {new_start_time}\n\
End Time   : {new_end_time}\n")

    input('Press Enter to continue...')
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
                while True:
                    validName = True
                    updateEventName = input("Enter a new event name: ")
                    for event in database:
                        if updateEventName.lower() == event[0].lower():
                            print('Name already taken')
                            validName = False
                            break
                    if validName:
                        break

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

                    # Copy Pasta everything in the database except the selected "eventINDEX"'s event into this Temporary List (for comparison).
                    tempDatabase = []
                    tempDatabase.extend(database)
                    del tempDatabase[eventINDEX]
                    
                    # Comparing 1st and 2nd Temporary List for clashing of Date, Location and Time all at once
                    clashFlag = checkEventTime(tempList, tempDatabase)
                    if clashFlag == True:
                        print("Clashing of Location, Date and Time with another existing event.")
                        print("Try again.")
                    elif clashFlag == 'Invalid time':
                        print("Invalid. End Time must come after Start Time.")
                    else:
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
                        updateEventDate = match.group(0)
                            
                        # To extract, then, copy pasta that one selected "eventINDEX"'s event into this 1st Temporary List (for comparison) and update it based on user input.
                        tempList = []
                        tempList.extend(database[eventINDEX])
                        tempList[3] = updateEventDate

                        # Copy Pasta everything in the database except the selected "eventINDEX"'s event into this Temporary List (for comparison).
                        tempDatabase = []
                        tempDatabase.extend(database)
                        del tempDatabase[eventINDEX]
                        
                        # Comparing 1st and 2nd Temporary List for clashing of Date, Location and Time all at once
                        clashFlag = checkEventTime(tempList, tempDatabase)
                        if clashFlag == True:
                            print("Clashing of Location, Date and Time with another existing event.")
                            print("Try again.")
                        elif clashFlag == 'Invalid time':
                            print("Invalid. End Time must come after Start Time.")
                        else:
                            database[eventINDEX][3] = updateEventDate
                            print(f"Event Date updated to '{updateEventDate}' !")
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
                            # Copy Pasta everything in the database except the selected "eventINDEX"'s event into this Temporary List (for comparison).
                            tempDatabase = []
                            tempDatabase.extend(database)
                            del tempDatabase[eventINDEX]
                            
                            # Comparing 1st and 2nd Temporary List for clashing of Date, Location and Time all at once
                            clashFlag = checkEventTime(tempList, tempDatabase)
                            if clashFlag == True:
                                print("Clashing of Location, Date and Time with another existing event.")
                                print("Try again.")
                            elif clashFlag == 'Invalid time':
                                print("Invalid. End Time must come after Start Time.")
                            else:
                                database[eventINDEX][4] = tempList[4]
                                database[eventINDEX][5] = tempList[5]
                                print("Event Start and End Time updated successfully!")

                            loop_Time = False

                        else:
                            print("Please try again.")
                    
                    else:
                        print("Try again. Choose 1, 2 or 3 only.")
                        
            # 6. Back to Main Menu
            elif updateChoice == 6:
                print("Back to Main Menu......")
                loop = False

            else:
                print("Enter valid options only. Try again.")

        else:
            print("Please try again. Enter digits only.")
        input('Press Enter to continue...')

    return database

# Delete existing event
def deleteEvent(database):
    delegroup= selectEvent(database)
    if delegroup == None:
        return database
    del database[delegroup]
    print("Event succcessfully deleted :)")
    input('Press Enter to continue...')
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
    input('Press Enter to continue...')

#Marking attendees system  
#Bismillah
#Simplified but works
def mark_attendance(attendees):
  """
  This function allows marking attendance for each attendee.

  Args:
      attendees: A list containing attendee names.

  Returns:
      A modified list of attendees with attendance status (present/absent).
  """
  for index, attendee in enumerate(attendees):
    print(f"{index+1}. {attendee}")
    status = input(f"Mark '{attendee}' as (P)resent or (A)bsent: ").upper()
    if status == "P":
      attendees[index] = f"{attendee} (Present)"
    elif status == "A":
      attendees[index] = f"{attendee} (Absent)"
    else:
      print("Invalid input. Please enter 'P' or 'A'.")
  return attendees

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
    if eventIndex == None:
        return database
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
                attendees = mark_attendance(attendees)

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

        input('Press Enter to continue...')

    database[eventIndex][6] = attendees
    return database


# Prints event schedule:
def printEventDetails(database):
    eventIndex = selectEvent(database)
    if eventIndex == None:
        return
    event = database[eventIndex]
    print('Name       :',event[0])
    print('Description:',event[1])
    print('Location   :',event [2])
    print('Date       :',event[3])
    print('Time Start :',event[4])
    print('       End :',event[5])
    j = ", ".join(event[6])
    print('Attendee   :',j)
    input('Press Enter to continue...')




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
        print('Thank you, have a good day! :)')
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
