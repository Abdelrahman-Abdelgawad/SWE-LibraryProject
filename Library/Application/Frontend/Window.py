from abc import ABC, abstractmethod
from Application.Backend.LibraryBackend import LibBackend

class Window(ABC):
    
    _backEnd = LibBackend()
    
    #------------- FrontEnd Methods ---------------------------

    @abstractmethod
    def updateTreeView (rows):
        pass
    
    #////////////////////////////////////////
    
    @abstractmethod
    def getRow(event): 
        pass
    
    #-------------------- Commands Methods ----------------------
        
    @abstractmethod
    def search():
       pass
   
    #////////////////////////////////////////
    
    @abstractmethod
    def updateRow():
       pass
    
    #////////////////////////////////////////
    
    @abstractmethod
    def addRow():
        pass
    
    #////////////////////////////////////////
    
    @abstractmethod
    def deleteRow():
        pass
    
    #////////////////////////////////////////
    
    @abstractmethod
    def ExecuteGUI():
        pass