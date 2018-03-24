from tkinter import *
import add
import remove
import update_db

def back(root,s):
	root.deiconify()
	s.destroy()
	
def update(root):
	u=Toplevel(root)
	u.title("Meeting Scheduler")
	u.minsize(640,200)
	l1 = Label(u,compound=CENTER,fg="black",bg="orange",height=2,text="Update",font="Bold 20")
	b1=Button(u,compound=LEFT,width=20,height=3,relief=GROOVE,font="Bold 15",text="Add New Meeting",command=lambda : add.add(u))
	b2=Button(u,compound=LEFT,width=20,height=3,relief=GROOVE,font="Bold 15",text="Update Existing Meeting",command=lambda : update_db.update_db(u))
	b3=Button(u,compound=LEFT,width=20,height=3,relief=GROOVE,font="Bold 15",text="Remove Meeting",command=lambda : remove.remove(u))
	b4=Button(u,compound=LEFT,width=20,height=3,relief=GROOVE,font="Bold 15",text="Back",command=lambda : back(root,u))
	l1.pack(fill=X)
	b1.pack(fill=X)
	b2.pack(fill=X)
	b3.pack(fill=X)
	b4.pack(fill=X)
	root.withdraw()
	u.mainloop()