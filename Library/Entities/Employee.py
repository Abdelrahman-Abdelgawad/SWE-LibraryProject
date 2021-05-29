from DataAccess.DBAffiliate import DBAffiliate

class Employee(DBAffiliate):
    
    def __init__(self):
        pass
    
    # Findall method that returns all the rows in an employee table
    def FindAll(self):
        employeeList = []
        queryStr = "select * from employee"
        
        try:
            self._conn.cr.execute(queryStr)
        
            for currentEmployee in self._conn.cr.fetchall():
                currentEmployeeTuple = (currentEmployee[0],
                                        currentEmployee[1],
                                        currentEmployee[2],
                                        currentEmployee[3],
                                        str(currentEmployee[4]),
                                        currentEmployee[5])
                
                employeeList.append(currentEmployeeTuple)
            
            return employeeList
        
        except Exception as ex:
            return "Couldn't get the required data due to: " + str(ex)
    
    #----------------------------------------------------
    
    # FindByID method that returns the specified row in an employee table
    def FindByID(self, ID):

        queryStr = "select * from employee where EmpID = '{0}'"
        
        try:
            self._conn.cr.execute(queryStr.format(ID))
            employee = self._conn.cr.fetchone()
            
            employeeTuple = (employee[0],
                             employee[1],
                             employee[2],
                             employee[3],
                             str(employee[4]),
                             employee[5])    
            return employeeTuple
        
        except Exception as ex:
            return "Couldn't get the required data due to: " + str(ex)
    
    #----------------------------------------------------
    
    # Insert method that inserts a row in an employee table
    def Insert(self, rowDict):
        queryStr = "insert into employee values ('{0}', '{1}', '{2}', '{3}', {4}, {5})"
        queryStr = queryStr.format(rowDict["EmpID"],
                                   rowDict["Name"],
                                   rowDict["Salary"],
                                   rowDict["Email"],
                                   rowDict["PhoneNum"],
                                   rowDict["BranchID"])
        try:
            self._conn.cr.execute(queryStr)
            self._conn.db.commit()
            retStr = "The employee is added successfully."
        except Exception as ex:
            retStr = "Couldn't add the provided employee due to: " + str(ex)
        finally:
            return retStr
        
    #----------------------------------------------------
    
    # Delete method that deletes a specified row in an employee table
    def Delete(self, ID):
        queryStr = "delete from employee where EmpID = '{0}'".format(ID)
        try:
            self._conn.cr.execute(queryStr)
            self._conn.db.commit()
            retStr = "The employee is deleted successfully."
        except Exception as ex:
            retStr = "Couldn't delete the provided employee due to: " + str(ex)
        finally:
            return retStr
            
    #----------------------------------------------------
    
    # Update method that updates a specified row in an employee table
    def Update(self, rowDict):
        queryStr = tmpStr = "update employee set "
        EmpID = rowDict["EmpID"]
        del rowDict["EmpID"]
        
        for item in rowDict.items():
            if item[1]:
                queryStr += "{0} = '{1}', ".format(item[0], item[1])
                
        if queryStr == tmpStr:
            retStr = "To ""update"" something, you should enter a new value!!"
        else:
            queryStr = queryStr[:len(queryStr)-2]
            queryStr += " where EmpID = '{0}'".format(EmpID)
            
            try:
                self._conn.cr.execute(queryStr)
                self._conn.db.commit()
                retStr = "The employee is updated successfully."
            except Exception as ex:
                retStr = "Couldn't update the provided employee due to: " + str(ex)
    
        return retStr
    
    #----------------------------------------------------
