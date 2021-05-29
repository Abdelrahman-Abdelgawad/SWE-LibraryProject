#------------------------------------------------
#
# Author: Abdelrahman Farouk 
#
# Date: 26-05-2021
#
#------------------------------------------------

from abc import ABC, abstractmethod
from Application.Backend.LibraryBackend import LibBackend

class Window(ABC):
    
    #Create an object of the backend class
    _backEnd = LibBackend()
    
    #------------- FrontEnd Methods ---------------------------
    
    # abstract method that will update the tree view in the window by the list of tuples passed to it
    @abstractmethod
    def updateTreeView (rows):
        pass
    
    
    # abstract method that will get the row of the tree view on double clicking on it
    @abstractmethod
    def getRow(event): 
        pass
    
    #-------------------- Commands Methods ----------------------
        
    # abstract method that will deploy the searching function 
    @abstractmethod
    def search():
       pass
   
    # abstract method that will deploy the updating function
    @abstractmethod
    def updateRow():
       pass
    
    # abstract method that will deploy the adding function
    @abstractmethod
    def addRow():
        pass
    
    # abstract method that will deploy the deleting function
    @abstractmethod
    def deleteRow():
        pass
    
    # abstract method that deploys the GUI executio
    @abstractmethod
    def ExecuteGUI():
        pass