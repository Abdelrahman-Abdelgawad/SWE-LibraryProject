import mysql.connector

class DBConnection():
    def __init__(self):
         self.db = mysql.connector.connect(host     = "localhost",
                                           database = "library",
                                           user     = "root",
                                           password = "root")
         self.cr = self.db.cursor()
    
    # Disconnect the connection form the MySQL server
    def Disconnect(self):
        self.db.close()

        

