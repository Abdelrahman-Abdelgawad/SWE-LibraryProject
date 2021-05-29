from DataAccess.DBAffiliate import DBAffiliate

from Entities.Book      import Book
from Entities.Employee  import Employee
from Entities.Member    import Member
from Entities.Branch    import Branch
from Entities.Borrowing import Borrowing
from Entities.Returning import Returning

# this class is for interfacing with the library database
class DBInterface(DBAffiliate):
    
    def __init__(self):
        pass
    
    #----------------------------------------------------
    
    """
    * Description: this private method takes the name of a table as a string, and returns an object of the table's class
    * takes:   string tableName
    * returns: object tableObj
    """
    def __findTableObj(self, tableName):
        
        if tableName == "book":
            tableObj = Book()
        elif tableName == "employee":
            tableObj = Employee()
        elif tableName == "member":
            tableObj = Member()
        elif tableName == "branch":
            tableObj = Branch()
        elif tableName == "borrowing":
            tableObj = Borrowing()
        elif tableName == "returning":
            tableObj = Returning()
        else:
            raise Exception("The passed table name is incorrect!")
        return tableObj
    
    #----------------------------------------------------
    
    """
    * Description: Findall method that returns all the rows in the provided table
    * takes:   string tableName
    * returns: List<Tuple> output or String exception
    """
    def FindAll(self, tableName):
        try:
            tableObj = self.__findTableObj(tableName)  # get an object of the table's class         
            output   = tableObj.FindAll()              # get a list of all the rows in the required table
            
            return output
        
        except Exception as ex:
            return str(ex) 
    
    #----------------------------------------------------
    
    """
    * Description: FindByID method that returns the specified row in the provided table
    * takes:   string tableName, string ID
    * returns: List<Tuple> output or String exception
    """
    def FindByID(self, tableName, ID):
        try:
            tableObj = self.__findTableObj(tableName)  # get an object of the table's class 
            output   = tableObj.FindByID(ID)           # get a dictionary of all the cells in the required row
            return output
        
        except Exception as ex:
            return str(ex)                             # return the exception message to user
        
    
    #----------------------------------------------------
    
    """
    * Description: Insert method that inserts a row in the provided table
    * takes:   string tableName, dictionary rowDict
    * returns: string retStr
    """
    def Insert(self, tableName, rowDict):
        retStr = ""                                    # return string which will contain the output of the method
        try:
            tableObj = self.__findTableObj(tableName)  # get an object of the table's class
            retStr = tableObj.Insert(rowDict)          # assign the insert status message to the return string
            
        except Exception as ex:
            retStr = str(ex)                           # assign the exception message to the return string
        finally:
            return retStr                              # return the return string
    
    #----------------------------------------------------
    
    """
    * Description: Delete method that deletes a specified row in the provided table
    * takes:   string tableName, string ID
    * returns: string retStr
    """
    def Delete(self, tableName, ID):
        retStr = ""                                    # return string which will contain the output of the method
        try:
            tableObj = self.__findTableObj(tableName)  # get an object of the table's class
            retStr = tableObj.Delete(ID)               # assign the Delete status message to the return string
            
        except Exception as ex:
            retStr = str(ex)                           # assign the exception message to the return string
        finally:
            return retStr                              # return the return string
    
    #----------------------------------------------------
    """
    * Description: Update method that updates a specified row in the provided table
    * takes:   string tableName, dictionary rowDict
    * returns: string retStr
    """
    def Update(self, tableName, rowDict):
        retStr = ""                                    # return string which will contain the output of the method
        try:
            tableObj = self.__findTableObj(tableName)  # get an object of the table's class
            retStr = tableObj.Update(rowDict)          # assign the update status message to the return string
            
        except Exception as ex:
            retStr = str(ex)                           # assign the exception message to the return string
        finally:
            return retStr                              # return the return string
      
    #----------------------------------------------------
    
    """
    * Description: Disconnect the connection form the MySQL server
    * takes: void
    * returns: void
    """
    def Disconnect(self):
        self._conn.Disconnect() # disconnect the connection form the MySQL server
      
    #----------------------------------------------------  