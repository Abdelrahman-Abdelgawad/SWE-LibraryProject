# -------------------------------------------------------------------------------
#
# Author: Elsayed Khaled Elsayed El-Refaei
#
# Date: 26-05-2021
#
# -------------------------------------------------------------------------------

from DataAccess.DBAffiliate import DBAffiliate


class Returning(DBAffiliate):

    def __init__(self):
        pass

    # Findall method that returns all the rows in an returning table
    def FindAll(self):
        returningsList = []
        queryStr = "select * from returning"

        try:
            self._conn.cr.execute(queryStr)

            for currentReturning in self._conn.cr.fetchall():
                returningTuple = (currentReturning[0],
                                  currentReturning[1],
                                  currentReturning[2],
                                  str(currentReturning[3]))
                returningsList.append(returningTuple)
            return returningsList

        except Exception as ex:
            return "Couldn't get the required data due to: " + str(ex)

    # ----------------------------------------------------

    # FindByID method that returns the specified row in an returning table
    def FindByID(self, ID):

        queryStr = "select * from returning where ReturnID = '{0}'"
        try:
            self._conn.cr.execute(queryStr.format(ID))
            returning = self._conn.cr.fetchone()

            returningTuple = (returning[0],
                              returning[1],
                              returning[2],
                              str(returning[3]))

            return returningTuple

        except Exception as ex:
            return "Couldn't get the required data due to: " + str(ex)

    # ----------------------------------------------------

    # Insert method that inserts a row in an returning table
    def Insert(self, rowDict):
        queryStr = "insert into returning values ('{0}', '{1}', '{2}', '{3}')"

        queryStr = queryStr.format(rowDict["ReturnID"],
                                   rowDict["BookISBN"],
                                   rowDict["MemID"],
                                   rowDict["ReturningDate"])

        try:
            self._conn.cr.execute(queryStr)
            self._conn.db.commit()
            retStr = "The returning is added successfully."
        except Exception as ex:
            retStr = "Couldn't add the provided returning due to: " + str(ex)
        finally:
            return retStr

    # ----------------------------------------------------

    # Delete method that deletes a specified row in an returning table
    def Delete(self, ID):
        queryStr = "delete from returning where ReturnID = '{0}'".format(ID)
        try:
            self._conn.cr.execute(queryStr)
            self._conn.db.commit()
            retStr = "The returning is deleted successfully."
        except Exception as ex:
            retStr = "Couldn't delete the provided returning due to: " + \
                str(ex)
        finally:
            return retStr

    # ----------------------------------------------------

    # Update method that updates a specified row in an returning table
    def Update(self, rowDict):
        queryStr = tmpStr = "update returning set "

        ReturnID = rowDict["ReturnID"]
        del rowDict["ReturnID"]

        for item in rowDict.items():
            if item[1]:
                queryStr += "{0} = '{1}', ".format(item[0], item[1])

        if queryStr == tmpStr:
            retStr = "To ""update"" something, you should enter a new value!!"

        else:
            queryStr = queryStr[:len(queryStr)-2]
            queryStr += " where ReturnID = '{0}'".format(ReturnID)

            try:
                self._conn.cr.execute(queryStr)
                self._conn.db.commit()
                retStr = "The returning is updated successfully."
            except Exception as ex:
                retStr = "Couldn't update the provided returning due to: " + \
                    str(ex)

        return retStr

    # ----------------------------------------------------
