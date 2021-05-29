from DataAccess.DBAffiliate import DBAffiliate

class Borrowing(DBAffiliate):
    
    def __init__(self):
        pass
    
    #----------------------------------------------------
    
    # Findall method that returns all the rows in an borrowing table
    def FindAll(self):
        borrowingsList = []
        queryStr = "select * from borrowing"
        
        try:
            self._conn.cr.execute(queryStr)
        
            for currentBorrowing in self._conn.cr.fetchall():
                
                currentBorrowingTuple = (currentBorrowing[0],
                                         currentBorrowing[1],
                                         currentBorrowing[2],
                                         str(currentBorrowing[3]))
                
                borrowingsList.append(currentBorrowingTuple)
                
            return borrowingsList
        
        except Exception as ex:
            return "Couldn't get the required data due to: " + str(ex)
    
    #----------------------------------------------------
    
    # FindByID method that returns the specified row in an borrowing table
    def FindByID(self, ID):
        
        queryStr = "select * from borrowing where BorrowID = '{0}'"
        try:
            self._conn.cr.execute(queryStr.format(ID))
            borrowing = self._conn.cr.fetchone()
            
            borrowingTuple = (borrowing[0],
                              borrowing[1],
                              borrowing[2],
                              str(borrowing[3]))
            
            return borrowingTuple
        
        except Exception as ex:
            return "Couldn't get the required data due to: " + str(ex)
    
    #----------------------------------------------------
    
    # Insert method that inserts a row in an borrowing table
    def Insert(self, rowDict):
        queryStr = "insert into borrowing values ('{0}', '{1}', '{2}', '{3}')"
        
        queryStr = queryStr.format(rowDict["BorrowID"],
                                   rowDict["BookISBN"],
                                   rowDict["MemID"],
                                   rowDict["BorrowingDate"])
        
        try:
            self._conn.cr.execute(queryStr)
            self._conn.db.commit()
            retStr = "The borrowing is added successfully."
        except Exception as ex:
            retStr = "Couldn't add the provided borrowing due to: " + str(ex)
        finally:
            return retStr
        
    #----------------------------------------------------
    
    # Delete method that deletes a specified row in an borrowing table
    def Delete(self, ID):
        queryStr = "delete from borrowing where BorrowID = '{0}'".format(ID)
        try:
            self._conn.cr.execute(queryStr)
            self._conn.db.commit()
            retStr = "The borrowing is deleted successfully."
        except Exception as ex:
            retStr = "Couldn't delete the provided borrowing due to: " + str(ex)
        finally:
            return retStr
            
    #----------------------------------------------------
    
    # Update method that updates a specified row in an borrowing table
    def Update(self, rowDict):
        queryStr = tmpStr = "update borrowing set "
        
        BorrowID = rowDict["BorrowID"]
        del rowDict["BorrowID"]
        
        for item in rowDict.items():
            if item[1]:
                queryStr += "{0} = '{1}', ".format(item[0], item[1])
                
        if queryStr == tmpStr:
            retStr = "To ""update"" something, you should enter a new value!!"
            
        else:
            queryStr = queryStr[:len(queryStr)-2]
            queryStr += " where BorrowID = '{0}'".format(BorrowID)
            
            try:
                self._conn.cr.execute(queryStr)
                self._conn.db.commit()
                retStr = "The borrowing is updated successfully."
            except Exception as ex:
                retStr = "Couldn't update the provided borrowing due to: " + str(ex)
    
        return retStr
    
    #----------------------------------------------------
    