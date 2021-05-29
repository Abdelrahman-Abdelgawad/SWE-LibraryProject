from tkinter import *
from DataAccess.DBInterface import DBInterface

class LibBackend():
    
    def __init__(self):
        self.DBI = DBInterface()       # this object will enable interaction with library database
        
    
    #////////////////////////////////////////

    """
    * Description: sets the table name variable
    * takes:       string tableName
    * returns:     void
    """
    def setTableName(self, tableName):
        self.tableName = tableName     # the required table name
        
    #////////////////////////////////////////

    """
    * Description: shows a string in an info message box
    * takes:       string msg
    * returns:     void
    """
    def __outputMsg(self, msg):
        messagebox.showinfo('information', msg)   #pops up a message box of type info to the user with the provided string as the message
    
    #////////////////////////////////////////
        
    """
    * Description: fill tree view with all the required table's data
    * takes:       void
    * returns:     void
    """
    def search(self, searchID):
        output = self.DBI.FindByID(self.tableName, searchID)  
        
        if(type(output) == str):                # if the type of the output is a string, this means that an exception has accured
           self.__outputMsg(output)
           return self.showAll()
        else:    
            return [output]                     # list of one row (required row) to be writen in the treeview, this is cuz updateTreeView takes a list of tuples
    
    #////////////////////////////////////////
    
    """
    * Description: shows all the tabel's records in the tree view
    * takes:       void
    * returns:     void
    """
    def showAll(self):
        rows = self.DBI.FindAll(self.tableName)
        
        if(type(rows) == str):                    # if the type of the output is a string, this means that an exception has accured
           self.__outputMsg(rows)
        else:    
            return rows
        
    #////////////////////////////////////////
    
    """
    * Description: gets all the selected row values 
    * takes:       void
    * returns:     void
    """
    def updateRow(self, currentRow):        
        msgTitle = "Confirm Update?"
        msg = "Are you sure you want to Update this particular row?"                
        confirmUpdate = messagebox.askyesno(msgTitle,msg)                # assigns the return value of the message box (update confirmation) to a variable to check it
        
        if confirmUpdate:                                                # checks if the user confirmed the updating; if so, update the data base with the values in the entry boxes, else, continue
            memberDict = currentRow.copy()
            for key in memberDict:
                memberDict[key] = memberDict[key].get()
            
            self.__outputMsg(self.DBI.Update(self.tableName, memberDict))  # updates the database values with the new values 
        return self.showAll()
     
    #////////////////////////////////////////
    
    """
    * Description: adds the entered row values to the database 
    * takes:       void
    * returns:     void
    """
    def addRow(self, currentRow):
        msgTitle = "Confirm Add?"
        msg = "Are you sure you want to Add this row?"                
        confirmAdd = messagebox.askyesno(msgTitle,msg)                # assigns the return value of the message box (add confirmation) to a variable to check it
        
        if confirmAdd:
            memberDict = currentRow.copy()
            
            for key in memberDict:
                memberDict[key] = memberDict[key].get()
                
            self.__outputMsg(self.DBI.Insert(self.tableName, memberDict))
        return self.showAll()
    
    #////////////////////////////////////////
    
    """
    * Description: deletes the selected row values rom the database 
    * takes:       void
    * returns:     void
    """
    def deleteRow(self, ID):
        msgTitle = "Confirm Delete?"
        msg = "Are you sure you want to Delete this particular row?"                
        confirmDelete = messagebox.askyesno(msgTitle,msg)                # assigns the return value of the message box (delete confirmation) to a variable to check it
        
        if confirmDelete:
            self.__outputMsg(self.DBI.Delete(self.tableName, ID))
        return self.showAll()
        
    #////////////////////////////////////////
    
    """
    * Description: Disconnect the connection form the MySQL server
    * takes: void
    * returns: void
    """
    def Disconnect(self):
        self.DBI.Disconnect() # disconnect the connection form the MySQL server
      
