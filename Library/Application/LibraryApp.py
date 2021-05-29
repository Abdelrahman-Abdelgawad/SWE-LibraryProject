from Frontend.BookWindow      import BookWindow
from Frontend.EmployeeWindow  import EmployeeWindow
from Frontend.MemberWindow    import MemberWindow
from Frontend.ReturningWindow import ReturningWindow
from Frontend.BorrowingWindow import BorrowingWindow
from Frontend.BranchWindow    import BranchWindow

from Backend.LibraryBackend   import LibBackend

userMsg = "Enter the number of the required record: \n" +\
          "For library books'       records enter >> 1 \n" +\
          "For library members'     records enter >> 2 \n" +\
          "For library employees'   records enter >> 3 \n" +\
          "For library borrwoings'  records enter >> 4 \n" +\
          "For library returnings'  records enter >> 5 \n" +\
          "For library branches'    records enter >> 6 \n" +\
          "To quit enter >> q \n"
             
while True:
    print(userMsg)
    userInput = input("Your Choice: ") 
    if userInput == "1":
        BookWindow().ExecuteGUI()
    elif userInput == "2":
        MemberWindow().ExecuteGUI()
    elif userInput == "3":
        EmployeeWindow().ExecuteGUI()
    elif userInput == "4":
        BorrowingWindow().ExecuteGUI()
    elif userInput == "5":
        ReturningWindow().ExecuteGUI()
    elif userInput == "6":
        BranchWindow().ExecuteGUI()
    elif userInput == "q":
        break
    else:
        print("Wrong Choice!!\n\n----------------------\n\n")

LibBackend().Disconnect()

