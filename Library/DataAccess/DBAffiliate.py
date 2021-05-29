#--------------------------
# Author: Sherif Gamal
#
# Date:   26-05-2021
#--------------------------

from abc import ABC, abstractmethod
from DataAccess.DBConnection import DBConnection

# this is an abstract class that contains all methods required for any Database interaction
class DBAffiliate(ABC):
    
    # database connection object to used to connect with the library database
    _conn = DBConnection()
    
    #----------------------------------------------------
    
    # this is an abstract method that returns all the rows in an entity
    @abstractmethod
    def FindAll(self):
        pass
    
    #----------------------------------------------------
    
    # this is an abstract method that returns the specified row in an entity
    @abstractmethod
    def FindByID(self, ID):
        pass
    
    #----------------------------------------------------
    
    # this is an abstract method that inserts a row in an entity
    @abstractmethod
    def Insert(self, rowDict):
        pass
    
    #----------------------------------------------------
    
    # this is an abstract method that deletes a specified row in an entity
    @abstractmethod
    def Delete(self, ID):
        pass
    
    #----------------------------------------------------
    
    # this is an abstract method that updates a specified row in an entity
    @abstractmethod
    def Update(self, rowDict):
        pass
      
    #----------------------------------------------------
      
    