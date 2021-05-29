#--------------------------------------------------
# Author: Abdelrahman Faruok
#
# Date:   26-05-2021
#
#--------------------------------------------------

from tkinter import *

from DataAccess.DBInterface import DBInterface

"""
* this class is as a backend to the library app
* and it's used to connect the forntend with the library database
"""
class LibBackend():
    
    def __init__(self):
        
        # this DBInterface object is used to interact with the library database
        self.DBI = DBInterface()       
        
    
    #////////////////////////////////////////////////////////////////////////////////

    """
    * Description: sets the table name variable, to the required table name
    * takes:       string tableName
    * returns:     void
    """
    def setTableName(self, tableName):
        
        # this attribute is used to indicate which table is reuried from all the library database tables.
        self.tableName = tableName     
        
    #////////////////////////////////////////////////////////////////////////////////

    """
    * Description: shows a string message in an info message box
    * takes:       string msg
    * returns:     void
    """
    def __outputMsg(self, msg):
        #pops up a message box of type info to the user with the provided message string
        messagebox.showinfo('information', msg)   
    
    #////////////////////////////////////////////////////////////////////////////////
        
    """
    * Description: get the required row from the database to be filled in the tree view
    * takes:       string searchID
    * returns:     list<tuple> | void
    """
    def search(self, searchID):
        
        # get the required row form the required table
        output = self.DBI.FindByID(self.tableName, searchID)  
        
        # if the type of the output is a string, 
        # this means that an exception has accured, and the operation didn't run as required
        if(type(output) == str):             
           self.__outputMsg(output) # pop a message box to user with the exception message
           return self.showAll()    # update the tree view
        else: 
            # return a list of one row (required row) to be writen in the treeview, 
            # this is done because the tree view takes a list of tuples, to be updated
            return [output]                     
    
    #////////////////////////////////////////////////////////////////////////////////
    
    """
    * Description: shows all the tabel's records in the tree view
    * takes:       void
    * returns:     list<tuple> | void
    """
    def showAll(self):
        
        # get sll the rows in the required table
        rows = self.DBI.FindAll(self.tableName)
        
        # if the type of the output is a string, 
        # this means that an exception has accured, and the operation didn't run as required
        if(type(rows) == str):                    
           self.__outputMsg(rows) # pop a message box to user with the exception message
        else:    
            return rows           # return list of all the rows in the required table
        
    #////////////////////////////////////////////////////////////////////////////////
    
    """
    * Description: gets all the selected row values 
    * takes:       dictionary currentRow
    * returns:     list<tuple> | void
    """
    def updateRow(self, currentRow):   
        
        msgTitle = "Confirm Update?"
        msg = "Are you sure you want to Update this particular row?" 
        
        # assigns the return value of the message box (update confirmation) to a variable to check it               
        confirmUpdate = messagebox.askyesno(msgTitle,msg)                
        
        # checks if the user confirmed the updating; 
        # if so, update the data base with the values in the entry boxes, else, continue
        if confirmUpdate:
            # take a copy form the user's currentRow dict
            # this is done to avoid changing the orginal user data, as they are stringVar                                               
            memberDict = currentRow.copy()              
            
            for key in memberDict:
                # get the string value in all the members of the MemberDict, 
                # this is done to change them from stringVar to string 
                memberDict[key] = memberDict[key].get()
            
            # updates the database values with the new values
            # and print to user the result in a message box
            self.__outputMsg(self.DBI.Update(self.tableName, memberDict))   
        
        # update the tree view
        return self.showAll() 
     
    #////////////////////////////////////////////////////////////////////////////////
    
    """
    * Description: adds the entered row values to the database 
    * takes:       dictionary currentRow
    * returns:     list<tuple> | void
    """
    def addRow(self, currentRow):
        msgTitle = "Confirm Add?"
        msg = "Are you sure you want to Add this row?"   

        # assigns the return value of the message box (add confirmation) to a variable to check it             
        confirmAdd = messagebox.askyesno(msgTitle,msg)                
        
        # checks if the user confirmed the updating; 
        # if so, update the data base with the values in the entry boxes, else, continue
        if confirmUpdate:
            # take a copy form the user's currentRow dict
            # this is done to avoid changing the orginal user data, as they are stringVar                                               
            memberDict = currentRow.copy()              
            
            for key in memberDict:
                # get the string value in all the members of the MemberDict, 
                # this is done to change them from stringVar to string 
                memberDict[key] = memberDict[key].get()
            
            # insert a row with the current values in the database
            # and print to user the result in a message box
            self.__outputMsg(self.DBI.Insert(self.tableName, memberDict))
        
        # update the tree view
        return self.showAll()
    
    #////////////////////////////////////////
    
    """
    * Description: deletes the selected row values rom the database 
    * takes:       string ID
    * returns:     list<tuple> | void
    """
    def deleteRow(self, ID):
        msgTitle = "Confirm Delete?"
        msg = "Are you sure you want to Delete this particular row?"   

        # assigns the return value of the message box (delete confirmation) to a variable to check it             
        confirmDelete = messagebox.askyesno(msgTitle,msg)                
        
        if confirmDelete:
            # Delete the required row form database
            # and print to user the result in a message box
            self.__outputMsg(self.DBI.Delete(self.tableName, ID))
            
        # update the tree view
        return self.showAll()
        
    #////////////////////////////////////////////////////////////////////////////////
    
    """
    * Description: Disconnect the connection form the MySQL server
    * takes:       void
    * returns:     void
    """
    def Disconnect(self):
        self.DBI.Disconnect() 
      
