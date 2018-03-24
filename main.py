from tkinter import *
from tkinter import messagebox
import view
import search
import update
import sqlite3

def help():
	s1="View Schedule : Shows the full schedule\n"
	s2="Update Schedule : Provides Updation Options\n" 
	s3="    ->Add New Meeting : Allows to add meetings\n"
	s4="    ->Update Existing Meeting : Select an Existing Meeting to Update\n"
	s5="    ->Remove Meeting : Select a Meeting to remove from Schedule\n"
	s6="Search Schedule : Allows to search for a particular meeting in schedule\n"
	s7="\nDate Format Used : yyyy-mm-dd"
	s8="\nTime Format Used : hh:mm"
	s9="\nPlease use correct formats otherwise Errors will be shown"
	messagebox.showinfo("HELP",s1+s2+s3+s4+s5+s6+s7+s8+s9)
	
root=Tk()
root.title("Meeting Scheduler")
root.minsize(640,200)

l1 = Label(root,compound=CENTER,fg="black",bg="yellow",height=2,text="MEETING SCHEDULER",font="Bold 20")
b1 = Button(root,compound=LEFT,width=20,height=3,relief=GROOVE,text="View Schedule",font="Bold 15",command=lambda : view.view(root))
b2 = Button(root,compound=LEFT,width=20,height=3,relief=GROOVE,text="Update Schedule",font="Bold 15",command=lambda : update.update(root))
b3 = Button(root,compound=LEFT,width=20,height=3,relief=GROOVE,text="Search Meeting",font="Bold 15",command=lambda : search.search(root))
b4 = Button(root,compound=LEFT,width=20,height=3,relief=GROOVE,text="Help",font="Bold 15",command=help)
b5 = Button(root,compound=LEFT,width=20,height=3,relief=GROOVE,text="Exit",font="Bold 15",command=root.destroy)

l1.pack(fill = X)
b1.pack(fill = X)
b2.pack(fill = X)
b3.pack(fill = X)
b4.pack(fill = X)
b5.pack(fill = X)

root.mainloop()

