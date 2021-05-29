from abc import ABC, abstractmethod
from DataAccess.DBConnection import DBConnection

# ------------
class DBAffiliate(ABC):
    # connection object to connect with the database
    _conn = DBConnection()
    
    #----------------------------------------------------
    
    # Findall method that returns all the rows in an entity
    @abstractmethod
    def FindAll(self):
        pass
    
    #----------------------------------------------------
    
    # FindByID method that returns the specified row in an entity
    @abstractmethod
    def FindByID(self, ID):
        pass
    
    #----------------------------------------------------
    
    # Insert method that inserts a row in an entity
    @abstractmethod
    def Insert(self, rowDict):
        pass
    
    #----------------------------------------------------
    
    # Delete method that deletes a specified row in an entity
    @abstractmethod
    def Delete(self, ID):
        pass
    
    #----------------------------------------------------
    
    # Update method that updates a specified row in an entity
    @abstractmethod
    def Update(self, rowDict):
        pass
      
    #----------------------------------------------------
      
    