from datetime import datetime



#importing text file into special list
#here we are reading it
def ReadTickets(FilePath):
  SpecialList = []
  try:
    with open(FilePath, "r") as file:
      for line in file:
        ticket_info = line.strip().split(", ")
        SpecialList.append(ticket_info)
  except FileNotFoundError:
    print(f"Error: '{FilePath}' file not found.")
  return SpecialList
#get the join function from stack overflow
#here we are saving the content into the special list
def SaveTickets(SpecialList):
    with open(FilePath, "w") as file:
        for ticket in SpecialList:
            file.write(", ".join(ticket))
def DisplayStatistics(SpecialList):
    event_tickets = {}
    for ticket_info in SpecialList:
        event_id = ticket_info[1]
        if event_id in event_tickets:
            event_tickets[event_id] += 1
        else:
            event_tickets[event_id] = 1
    if not event_tickets:
        print("There is 0 tickets .")
        return
    # the max funtion written by the help of:https://thepythonguru.com/python-builtin-functions/max/
    max_event_id = max(event_tickets, key=event_tickets.get)
    max_tickets = event_tickets[max_event_id]
    print(f"The event ID with the highest number of tickets is {max_event_id} with {max_tickets} tickets.")  
#the parameters needed to book a new ticket
def BookTicket(SpecialList, event_id, timestamp, username, priority=0):
    ticket_id = get_next_ticket_id(SpecialList)
    SpecialList.append([ticket_id, event_id, username, timestamp,str(priority)])
    print("Done!")
  
def get_next_ticket_id(tickets):
    if not tickets:
        return "tick101"
    last_ticket_id = tickets[-1][0]
    num = int(last_ticket_id[4:])
    return f"tick{num + 1:03}"
  #then the entered info will be saved in the special list created
    print("Done!")
def DisplayTicket(SpecialList):
    # 3 and 1 represent the index of event id and date in the list
    sorted_tickets = sorted(SpecialList, key=lambda x: (x[3], x[1]))
    today = datetime.now().strftime("%Y%m%d")
   #this loop to get the dates from today
    for ticket_info in sorted_tickets:
        if ticket_info[3] >= today:
            print(", ".join(ticket_info))

def ChangePriority(SpecialList, ticket_id, priority):
    for ticket_info in SpecialList:
        if ticket_info[0] == ticket_id:
            ticket_info[4] = str(priority)
            print("Done!")
          
        else:
          print("Ticket not found.")

def RemoveTicket(SpecialList, ticket_id):
    for ticket_info in SpecialList:
        if ticket_info[0] == ticket_id:
            tickets.remove(ticket_info)
            print("Done!")
            return
    print("Ticket not found.")
#https://www.programiz.com/python-programming/datetime
def TodayEvents(SpecialList):
    today = datetime.now().strftime("%Y%m%d")
    today_tickets = [ticket_info for ticket_info in SpecialList if ticket_info[3] == today]
    if not today_tickets:
        print("No events today.")
        return

    sorted_tickets = sorted(today_tickets, key=lambda x: int(x[4]), reverse=True)
    for ticket_info in sorted_tickets:
        print(f"Running event: {ticket_info[1]}, Ticket ID: {ticket_info[0]}, Priority: {ticket_info[4]}")
        tickets.remove(ticket_info)
def AdminMenu(SpecialList):
  #the while loop is to let the menu display again
  while True:
    print("\n\nAdmin Menu : \n\n" + "1. Display Statistics\n" + "2. Book a Ticket\n"+"3. Display all Tickets\n"+"4. Change Ticket's Priority\n"+"5. Disable Ticket\n"+"6. Run Events\n"+"7. Exit\n")
    choice = input("Enter your choice number: ")
    if choice == "1" :
      DisplayStatistics(SpecialList)
    elif choice == "2" :
      event_id = input("Enter the event ID : ")
      timestamp = input("Enter the time : ")
      priority = input("Enter the priority : ")
      BookTicket(SpecialList, event_id, timestamp, "admin", priority)
    elif choice == "3":
      DisplayTicket(SpecialList)
    elif choice == "4":
      ticket_id = input("Enter the ticket ID: ")
      priority = input("Enter the new priority: ")
      ChangePriority(SpecialList, ticket_id, priority)
    elif choice == "5":
      ticket_id = input("Enter the ticket ID: ")
      RemoveTicket(SpecialList, ticket_id)
    elif choice == "6":
      TodayEvents(SpecialList)
    elif choice == "7":
      SaveTickets(SpecialList)
      break
    else:
      print("choose from 1 to 7 only")
def UserMenu(SpecialList):
  while True:
    print("\n\nUser Menu :\n"+"1.Book a Ticket\n"+"2. Exit\n")
    choice = input("Enter your choice number: ")
    if choice == "1":
      event_id = input("Enter the event ID: ")
      timestamp = input("Enter the timestamp: ")
      BookTicket(SpecialList, event_id, timestamp, "user")
    elif choice == "2":
      SaveTickets(SpecialList)
      break
    else:
      print("You can only choose 1 or 2") 
if __name__ == "__main__":
  FilePath = "tickets.txt"
  SpecialList = ReadTickets(FilePath)
  print ("Please login and leave the password empty if you are a user")
  username = input("Username : ")
  password = input("Password : ")
  if username == "admin" and password == "admin123123":
    AdminMenu(SpecialList)
  elif username!= "admin" and password == "":
    UserMenu(SpecialList)
  else :
    print("Incorrect Username and/or Password")
  
