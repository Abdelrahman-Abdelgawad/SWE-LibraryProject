# -------------------------------------------------------------------------------
#
# Author: Attia Sayed Attia
#
# Date: 26-05-2021
#
# -------------------------------------------------------------------------------


from tkinter import *
from tkinter import ttk
import tkinter as tk

from Application.Frontend.Window import Window

class BranchWindow(Window):
    
    def __init__(self):
        self._backEnd.setTableName("branch")

    #------------- FrontEnd Methods ---------------------------
    
    """
    * Description: update the tree view version
    * takes:       list<tuple> rows
    * returns:     void
    """
    def updateTreeView (self, rows):
        self.trv.delete(*self.trv.get_children())      # delete the last treeview table version
        
        for i in rows:                                 # for each row in the passed rows
            self.trv.insert('','end',values = i)       # add the current row to the treeview table 
    
    #////////////////////////////////////////
    
    """
    * Description: gets all the selected row values 
    * takes:       event (a double click on a row of the tree view)
    * returns:     void
    """
    def getRow(self, event): 
        item = self.trv.item(self.trv.focus())
        
        i = 0
        # set the values of the current row to a dictionary to use it in the entry section
        for key in self.CurrentRow:
            self.CurrentRow[key].set(item['values'][i])
            i += 1
    
    
    #-------------------- Commands Methods ----------------------
        
    """
    * Description: fill tree view with all the required table's data
    * takes:       void
    * returns:     void
    """
    def search(self):
        self.updateTreeView(self._backEnd.search(self.SearchID.get()))
    
    #////////////////////////////////////////
    
    """
    * Description: gets all the selected row values 
    * takes:       void
    * returns:     void
    """
    def updateRow(self):
        self.updateTreeView(self._backEnd.updateRow(self.CurrentRow))
    
    
    #////////////////////////////////////////
    
    
    """
    * Description: adds the entered row values to the database 
    * takes:       void
    * returns:     void
    """
    def addRow(self):
        self.updateTreeView(self._backEnd.addRow(self.CurrentRow))
    
    
    #////////////////////////////////////////
    
    
    """
    * Description: deletes the selected row values rom the database 
    * takes:       void
    * returns:     void
    """
    def deleteRow(self):
        idKey = list(self.CurrentRow.keys())[0]
        self.updateTreeView(self._backEnd.deleteRow(self.CurrentRow[idKey].get()))


    #---------------------- GUI ----------------------------------

    
    def ExecuteGUI(self):

        root = Tk()
        
        root.title("Library branches' records")
        root.geometry("1920x1080")
        root.configure(bg="#cdcdcd")
        
        
        self.SearchID = StringVar()
        self.CurrentRow = {}
        
        self.CurrentRow["BranchID"]    = StringVar()
        self.CurrentRow["Address"]     = StringVar()
        
        
                        
        wrapper1 = LabelFrame(root, text="Records", font=("Engravers MT",20,"bold"), bg="#cdcdcd")
        wrapper2 = LabelFrame(root, text="Search", font=("Engravers MT",20,"bold"), bg="#cdcdcd")
        wrapper3 = LabelFrame(root, text="Modify", font=("Engravers MT",20,"bold"), bg="#cdcdcd")
        
        wrapper1.pack(fill="both", expand="yes", padx= 20, pady=10)
        wrapper2.pack(fill="both", expand="yes",padx=20, pady = 10)
        wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)
        
        
        
        
        #---------------------------- Wrapper 1 ----------------------
        
        tree_scroll = Scrollbar(wrapper1)
        tree_scroll.pack(side=RIGHT, fill=Y)
        
        self.trv = ttk.Treeview(wrapper1, columns=(1,2), show ="headings", height="6", yscrollcommand =tree_scroll.set)
        self.trv.pack(fill="both", expand="yes")
        
        self.trv.heading(1, text="Branch ID")
        self.trv.heading(2, text="Address")
        
        
        tree_scroll.config(command = self.trv.yview)
        
        self.trv.bind('<Double 1>', self.getRow)
        
        
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Bahnschrift Condensed", 16))
        
        #---------------------------- Wrapper 2 ----------------------
        
        lbl = Label(wrapper2, text="Search",font=("Berlin Sans FB Demi",16),bg="#cdcdcd")
        lbl.pack(side=tk.LEFT, padx= 10)
        
        ent = Entry(wrapper2, textvariable = self.SearchID,font=("PT Bold Heading",16))
        ent.pack(side=tk.LEFT, padx=6)
        
        btn = Button(wrapper2, text="Search" , command = self.search,bd=0)
        btn.pack(side=tk.LEFT, padx=6)
        
        
        #---------------------------- Wrapper 3 ----------------------
        
        
        lbl1 = Label(wrapper3, text="Branch ID: ", font=("Berlin Sans FB Demi",16),bg="#cdcdcd")
        lbl1.grid ( row=0, column=0, padx=5, pady=3)
        
        ent1= Entry(wrapper3, textvariable = self.CurrentRow["BranchID"] ,font=("PT Bold Heading",16))
        ent1.grid(row=0, column=1, padx=5, pady=3)
        
        lbl2 = Label(wrapper3, text="Address: " ,font=("Berlin Sans FB Demi",16),bg="#cdcdcd")
        lbl2.grid(row=0, column=3, padx=5, pady=3)
        
        ent2 = Entry(wrapper3, textvariable = self.CurrentRow["Address"],font=("PT Bold Heading",16))
        ent2.grid(row=0, column=4, padx=5, pady=3)
        
        
        up_btn =Button(wrapper3, text="update" , command = self.updateRow,bd=0)
        
        add_btn= Button(wrapper3, text="add" ,command = self.addRow,bd=0)
        
        delete_btn = Button(wrapper3, text="delete" ,command = self.deleteRow,bd=0)
        
        add_btn.place(x=220, y=80)
        up_btn.place(x=420, y=80)
        delete_btn.place(x=620, y=80)
        
        lbl_list = Label(wrapper3,bd=0)
        lbl_list.place(x=620)
        
        self.updateTreeView(self._backEnd.showAll())
        
        root.mainloop()
                

        