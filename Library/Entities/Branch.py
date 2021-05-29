from DataAccess.DBAffiliate import DBAffiliate

class Branch(DBAffiliate):
    
    def __init__(self):
        pass
    
    #----------------------------------------------------
    
    # Findall method that returns all the rows in an branch table
    def FindAll(self):
        branchsList = []                    # this list will contain all the rows in the branch table
        queryStr = "select * from branch"   # SQL query, select all rows in the branch table
        
        try:
            self._conn.cr.execute(queryStr)                 # execute the SQL query
        
            for currentBranch in self._conn.cr.fetchall():  # for each row in the branch table
                currentBranchTuple = (currentBranch[0],
                                      currentBranch[1])
                
                branchsList.append(currentBranchTuple)       # add the current row to the branch list
            return branchsList                              # return list of all rows in the branch table
        
        except Exception as ex:
            return "Couldn't get the required data due to: " + str(ex)  # return the excption massege to user as str
    
    #----------------------------------------------------
    
    # FindByID method that returns the specified row in an branch table
    def FindByID(self, ID):
                                       
        queryStr = "select * from branch where BranchID = '{0}'"  # SQL qurey, select all cells in the row with the passed branch id
        try:
            self._conn.cr.execute(queryStr.format(ID))      # execute the SQL query
            branch = self._conn.cr.fetchone()                     # get the selected row
            
            branchTuple = (branch[0],
                           branch[1])
            return branchTuple                                     # return dict of all cells in the required row
        
        except Exception as ex:
            return "Couldn't get the required data due to: " + str(ex)  # return the excption massege to user as str
    
    #----------------------------------------------------
    
    # Insert method that inserts a row in an branch table
    def Insert(self, rowDict):
        queryStr = "insert into branch values ('{0}', '{1}')"   # this dict will contain all cells in the required row in the branch table
        queryStr = queryStr.format(rowDict["BranchID"],      # SQL qurey, select all cells in the row with the passed branch id
                                   rowDict["Address"])
        try:
            self._conn.cr.execute(queryStr)               # execute SQL query
            self._conn.db.commit()                        # save the updates in the database
            retStr = "The branch is added successfully."  # assign successfull message to return string
            
        except Exception as ex:
            retStr = "Couldn't add the provided branch due to: " + str(ex) # assigh the exception message to return string
            
        finally:
            return retStr  # return the return string
        
    #----------------------------------------------------
    
    # Delete method that deletes a specified row in an branch table
    def Delete(self, ID):
        queryStr = "delete from branch where BranchID = '{0}'".format(ID)  # SQL query, delete the required branch from the branch table
        try:
            self._conn.cr.execute(queryStr)                 # execute SQL qurey
            self._conn.db.commit()                          # save the updates in the database
            retStr = "The branch is deleted successfully."    # assign successfull message to return string
        except Exception as ex:
            retStr = "Couldn't add the provided branch due to: " + str(ex) # assigh the exception message to return string
        finally:
            return retStr  # return the return string
            
    #----------------------------------------------------
    
    # Update method that updates a specified row in an branch table
    def Update(self, rowDict):
        queryStr = tmpStr = "update branch set " # SQL query, update the required branch in the branch table
        
        BranchID = rowDict["BranchID"]        # save the required Branch ID, as this will be deleted form the passed branch dict
        del rowDict["BranchID"]               # delete the branch ID form the passed branch dict, this is done to avoid adding it in the sql query
        
        for item in rowDict.items():                              # for each (Key,Value) in the passed branch dict
            if item[1]:                                              # if the value of the current cell is NOT null NOR empty
                queryStr += "{0} = '{1}', ".format(item[0], item[1]) # add the current cell to the update SQL qurey
                
        if queryStr == tmpStr:                                                 # if sql qurey string didn't change, which means all the values in the passed branch dict was empty
            retStr = "To ""update"" something, you should enter a new value!!" # assgin a notification message to the retrun string
            
        else:                                                       # some cells values wasn't empty
            queryStr = queryStr[:len(queryStr)-2]                   # remove the last two characters ", " from the SQL query
            queryStr += " where BranchID = '{0}'".format(BranchID)  # add the condition to the sql query, to update only the required branch
            
            try:
                self._conn.cr.execute(queryStr)                 # execute SQL qurey
                self._conn.db.commit()                          # save the updates in the database
                retStr = "The branch is updated successfully."    # assign successfull message to return string
            except Exception as ex:
                retStr = "Couldn't add the provided branch due to: " + str(ex) # assigh the exception message to return string   
        return retStr    # return the return string
    
    #----------------------------------------------------