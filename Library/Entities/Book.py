from DataAccess.DBAffiliate import DBAffiliate

class Book(DBAffiliate):
    
    def __init__(self):
        pass
    
    # Findall method that returns all the rows in an book table
    def FindAll(self):
        booksList = []
        queryStr = "select * from book"
        
        try:
            self._conn.cr.execute(queryStr)
        
            for currentBook in self._conn.cr.fetchall():
                currentBookTuple = (currentBook[0],
                                    currentBook[1],
                                    currentBook[2],
                                    currentBook[3],
                                    str(currentBook[4]),
                                    currentBook[5])
                
                booksList.append(currentBookTuple)
            
            return booksList
        
        except Exception as ex:
            return "Couldn't get the required data due to: " + str(ex)
    
    #----------------------------------------------------
    
    # FindByID method that returns the specified row in an book table
    def FindByID(self, ID):

        queryStr = "select * from book where ISBN = '{0}'"
        
        try:
            self._conn.cr.execute(queryStr.format(ID))
            book = self._conn.cr.fetchone()
            
            memberTuple = (book[0],
                           book[1],
                           book[2],
                           book[3],
                           str(book[4]),
                           book[5])    
            return memberTuple
        
        except Exception as ex:
            return "Couldn't get the required data due to: " + str(ex)
    
    #----------------------------------------------------
    
    # Insert method that inserts a row in an book table
    def Insert(self, rowDict):
        queryStr = "insert into book values ('{0}', '{1}', '{2}', '{3}', {4}, {5})"
        queryStr = queryStr.format(rowDict["ISBN"],
                                   rowDict["Title"],
                                   rowDict["Author"],
                                   rowDict["Publisher"],
                                   rowDict["NumOfCopies"],
                                   rowDict["LatencyFinePerDay"])
        try:
            self._conn.cr.execute(queryStr)
            self._conn.db.commit()
            retStr = "The book is added successfully."
        except Exception as ex:
            retStr = "Couldn't add the provided book due to: " + str(ex)
        finally:
            return retStr
        
    #----------------------------------------------------
    
    # Delete method that deletes a specified row in an book table
    def Delete(self, ID):
        queryStr = "delete from book where ISBN = '{0}'".format(ID)
        try:
            self._conn.cr.execute(queryStr)
            self._conn.db.commit()
            retStr = "The book is deleted successfully."
        except Exception as ex:
            retStr = "Couldn't delete the provided book due to: " + str(ex)
        finally:
            return retStr
            
    #----------------------------------------------------
    
    # Update method that updates a specified row in an book table
    def Update(self, rowDict):
        queryStr = tmpStr = "update book set "
        ISBN = rowDict["ISBN"]
        del rowDict["ISBN"]
        
        for item in rowDict.items():
            if item[1]:
                queryStr += "{0} = '{1}', ".format(item[0], item[1])
                
        if queryStr == tmpStr:
            retStr = "To ""update"" something, you should enter a new value!!"
        else:
            queryStr = queryStr[:len(queryStr)-2]
            queryStr += " where ISBN = '{0}'".format(ISBN)
            
            try:
                self._conn.cr.execute(queryStr)
                self._conn.db.commit()
                retStr = "The book is updated successfully."
            except Exception as ex:
                retStr = "Couldn't update the provided book due to: " + str(ex)
    
        return retStr
    
    #----------------------------------------------------
    