from DataAccess.DBAffiliate import DBAffiliate

# this class is for the "Member" Table in the DB
class Member(DBAffiliate):  
    
    def __init__(self):
        pass
    
    #----------------------------------------------------
    
    # Findall method that returns all the rows in a member table
    def FindAll(self):
        membersList = []                    # this list will contain all the rows in the member table
        queryStr = "select * from member"   # SQL query, select all rows in the member table
        
        try:
            self._conn.cr.execute(queryStr)                 # execute the SQL query
        
            for currentMember in self._conn.cr.fetchall():  # for each row in the member table
                currentMemberTuple = (currentMember[0],
                                      currentMember[1],
                                      currentMember[2],
                                      currentMember[3],
                                      str(currentMember[4]),
                                      currentMember[5])
                
                membersList.append(currentMemberTuple)       # add the current row to the members list
            return membersList                               # return list of all rows in the member table
     
        except Exception as ex:
            return "Couldn't get the required data due to: " + str(ex)  # return the excption massege to user as str
    
    #----------------------------------------------------
    
    # FindByID method that returns the specified row in a member table
    def FindByID(self, ID):
        
        queryStr = "select * from member where MemID = '{0}'"   # SQL qurey, select all cells in the row with the passed member id
        try:
            self._conn.cr.execute(queryStr.format(ID))       # execute the SQL query         
            member = self._conn.cr.fetchone()                   # get the selected row
            
            memberTuple = (member[0],
                           member[1],
                           member[2],
                           member[3],
                           str(member[4]),
                           member[5]) 
            
            return memberTuple                                   # return tuple of all cells in the required row
        except Exception as ex:
            return "Couldn't get the required data due to: " + str(ex)  # return the excption massege to user as str
    
    #----------------------------------------------------
    
    # Insert method that inserts a row in a member table
    def Insert(self, rowDict):
        queryStr = "insert into member values ({0}, '{1}', '{2}', '{3}', '{4}', {5})" # SQL query, insert the passed member in the member table
        queryStr = queryStr.format(rowDict["MemID"],
                                   rowDict["Name"],
                                   rowDict["PhoneNum"],
                                   rowDict["Email"],
                                   rowDict["RegDate"],
                                   rowDict["BranchID"])
        try:
            self._conn.cr.execute(queryStr)               # execute SQL query
            self._conn.db.commit()                        # save the updates in the database
            retStr = "The member is added successfully."  # assign successfull message to return string
        except Exception as ex:
            retStr = "Couldn't add the provided member due to: " + str(ex) # assigh the exception message to return string
        finally:
            return retStr  # return the return string
        
    #----------------------------------------------------
    
    # Delete method that deletes a specified row in a member table
    def Delete(self, ID):
        queryStr = "delete from member where MemID = '{0}'".format(ID)  # SQL query, delete the required member from the member table
        try:
            self._conn.cr.execute(queryStr)                 # execute SQL qurey
            self._conn.db.commit()                          # save the updates in the database
            retStr = "The member is deletd successfully."    # assign successfull message to return string
        except Exception as ex:
            retStr = "Couldn't delete the provided member due to: " + str(ex) # assigh the exception message to return string
        finally:
            return retStr  # return the return string
            
    #----------------------------------------------------
    
    # Update method that updates a specified row in a member table
    def Update(self, rowDict):
        queryStr = tmpStr = "update member set "  # SQL query, update the required member in the member table
        
        MemID = rowDict["MemID"]               # save the required member ID, as this will be deleted form the passed member dict
        del rowDict["MemID"]                   # delete the member ID form the passed member dict, this is done to avoid adding it in the sql query
        
        for item in rowDict.items():                              # for each (Key,Value) in the passed member dict
            if item[1]:                                              # if the value of the current cell is NOT null NOR empty
                queryStr += "{0} = '{1}', ".format(item[0], item[1]) # add the current cell to the update SQL qurey
                
        if queryStr == tmpStr:                                                 # if sql qurey string didn't change, which means all the values in the passed member dict was empty
            retStr = "To ""update"" something, you should enter a new value!!" # assgin a notification message to the retrun string
        else:                                                # some cells values wasn't empty
            queryStr = queryStr[:len(queryStr)-2]            # remove the last two characters ", " from the SQL query
            queryStr += " where MemID = '{0}'".format(MemID) # add the condition to the sql query, to update only the required member
            
            try:
                self._conn.cr.execute(queryStr)                 # execute SQL qurey
                self._conn.db.commit()                          # save the updates in the database
                retStr = "The member is updated successfully."  # assign successfull message to return string
            except Exception as ex:
                retStr = "Couldn't update the provided member due to: " + str(ex) # assigh the exception message to return string   
        return retStr    # return the return string
    
    #----------------------------------------------------