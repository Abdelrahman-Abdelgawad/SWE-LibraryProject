# -------------------------------------------------------------------------------
#
# Author: Elsayed Khaled Elsayed El-Refaei
#
# Date: 26-05-2021
#
# -------------------------------------------------------------------------------
from DataAccess.DBAffiliate import DBAffiliate


class Branch(DBAffiliate):

    def __init__(self):
        pass

    # ----------------------------------------------------

    # Findall method that returns all the rows in an branch table
    def FindAll(self):
        # this list will contain all the rows in the branch table
        branchsList = []
        # SQL query, select all rows in the branch table
        queryStr = "select * from branch"

        try:
            # execute the SQL query
            self._conn.cr.execute(queryStr)

            for currentBranch in self._conn.cr.fetchall():  # for each row in the branch table
                currentBranchTuple = (currentBranch[0],
                                      currentBranch[1])

                # add the current row to the branch list
                branchsList.append(currentBranchTuple)
            # return list of all rows in the branch table
            return branchsList

        except Exception as ex:
            # return the excption massege to user as str
            return "Couldn't get the required data due to: " + str(ex)

    # ----------------------------------------------------

    # FindByID method that returns the specified row in an branch table
    def FindByID(self, ID):

        # SQL qurey, select all cells in the row with the passed branch id
        queryStr = "select * from branch where BranchID = '{0}'"
        try:
            # execute the SQL query
            self._conn.cr.execute(queryStr.format(ID))
            branch = self._conn.cr.fetchone()                     # get the selected row

            branchTuple = (branch[0],
                           branch[1])
            # return dict of all cells in the required row
            return branchTuple

        except Exception as ex:
            # return the excption massege to user as str
            return "Couldn't get the required data due to: " + str(ex)

    # ----------------------------------------------------

    # Insert method that inserts a row in an branch table
    def Insert(self, rowDict):
        # this dict will contain all cells in the required row in the branch table
        queryStr = "insert into branch values ('{0}', '{1}')"
        queryStr = queryStr.format(rowDict["BranchID"],      # SQL qurey, select all cells in the row with the passed branch id
                                   rowDict["Address"])
        try:
            self._conn.cr.execute(queryStr)               # execute SQL query
            self._conn.db.commit()                        # save the updates in the database
            # assign successfull message to return string
            retStr = "The branch is added successfully."

        except Exception as ex:
            retStr = "Couldn't add the provided branch due to: " + \
                str(ex)  # assigh the exception message to return string

        finally:
            return retStr  # return the return string

    # ----------------------------------------------------

    # Delete method that deletes a specified row in an branch table
    def Delete(self, ID):
        # SQL query, delete the required branch from the branch table
        queryStr = "delete from branch where BranchID = '{0}'".format(ID)
        try:
            self._conn.cr.execute(queryStr)                 # execute SQL qurey
            self._conn.db.commit()                          # save the updates in the database
            # assign successfull message to return string
            retStr = "The branch is deleted successfully."
        except Exception as ex:
            retStr = "Couldn't add the provided branch due to: " + \
                str(ex)  # assigh the exception message to return string
        finally:
            return retStr  # return the return string

    # ----------------------------------------------------

    # Update method that updates a specified row in an branch table
    def Update(self, rowDict):
        # SQL query, update the required branch in the branch table
        queryStr = tmpStr = "update branch set "

        # save the required Branch ID, as this will be deleted form the passed branch dict
        BranchID = rowDict["BranchID"]
        # delete the branch ID form the passed branch dict, this is done to avoid adding it in the sql query
        del rowDict["BranchID"]

        for item in rowDict.items():                              # for each (Key,Value) in the passed branch dict
            # if the value of the current cell is NOT null NOR empty
            if item[1]:
                # add the current cell to the update SQL qurey
                queryStr += "{0} = '{1}', ".format(item[0], item[1])

        # if sql qurey string didn't change, which means all the values in the passed branch dict was empty
        if queryStr == tmpStr:
            # assgin a notification message to the retrun string
            retStr = "To ""update"" something, you should enter a new value!!"

        else:                                                       # some cells values wasn't empty
            # remove the last two characters ", " from the SQL query
            queryStr = queryStr[:len(queryStr)-2]
            # add the condition to the sql query, to update only the required branch
            queryStr += " where BranchID = '{0}'".format(BranchID)

            try:
                # execute SQL qurey
                self._conn.cr.execute(queryStr)
                self._conn.db.commit()                          # save the updates in the database
                # assign successfull message to return string
                retStr = "The branch is updated successfully."
            except Exception as ex:
                retStr = "Couldn't add the provided branch due to: " + \
                    str(ex)  # assigh the exception message to return string
        return retStr    # return the return string

    # ----------------------------------------------------
