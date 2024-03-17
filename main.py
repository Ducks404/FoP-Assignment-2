import re

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
                    updateEventAttendeeName =input("Your choice: ")

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