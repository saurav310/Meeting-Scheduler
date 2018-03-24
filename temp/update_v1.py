from tkinter import *
import sqlite3
import ctypes
c = sqlite3.connect('meeting.db')

def back(root,s):
	root.deiconify()
	s.destroy()

def store(e1,e2,e3,e4):
	print(e1.get())
	print(e2.get())
	print(e3.get())
	print(e4.get())
        #c.execute('''insert into meeting (project_name, meeting_time, meeting_date, meeting_topic) values ( ?,?,?,? )''',(e3.get(),e2.get(),e1.get(),e4.get()))
        #c.commit()

def new(u):
	n=Toplevel(u)
	n.title("New Entry")
	lt1=Label(n,text="Date").grid(row=1,column=0)
	e1=Entry(n).grid(row=1,column=1)
	lt2=Label(n,text="Time").grid(row=2,column=0)
	e2=Entry(n).grid(row=2,column=1)
	lt3=Label(n,text="Project Name").grid(row=3,column=0)
	e3=Entry(n).grid(row=3,column=1)
	lt4=Label(n,text="Topic").grid(row=4,column=0)
	e4=Entry(n).grid(row=4,column=1)
	b1=Button(n,text="Add",command=lambda : store(e1,e2,e3,e4)).grid(row=5,column=0)
	b2=Button(n,text="Back",command=lambda : back(u,n)).grid(row=5,column=1)
	u.withdraw()
	n.mainloop()

def change(ans,e1,e2,e4,v1=1,v2=1,v4=1):
	if v4.get()==0 and v2.get()==0 and v1.get()==1:
		c.execute('''update meeting set meeting_time = ? where project_name = ?''',(e1.get(),ans))
		c.commit()
	if v4.get()==0 and v2.get()==1 and v1.get()==0:
		c.execute('''update meeting set meeting_date = ? where project_name = ?''',(e2.get(),ans))
		c.commit()
	if v4.get()==1 and v2.get()==0 and v1.get()==0:
		c.execute('''update meeting set meeting_topic = ? where project_name = ?''',(e4.get(),ans))
		c.commit()
	if v4.get()==0 and v2.get()==1 and v1.get()==1:
		c.execute('''update meeting set meeting_time = ? where project_name = ?''',(e1.get(),ans))
		c.execute('''update meeting set meeting_date = ? where project_name = ?''',(e2.get(),ans))
		c.commit()
	if v4.get()==1 and v2.get()==1 and v1.get()==0:
		c.execute('''update meeting set meeting_date = ? where project_name = ?''',(e2.get(),ans))
		c.execute('''update meeting set meeting_topic = ? where project_name = ?''',(e4.get(),ans))
		c.commit()
	if v4.get()==1 and v2.get()==0 and v1.get()==1:
		c.execute('''update meeting set meeting_topic = ? where project_name = ?''',(e4.get(),ans))
		c.execute('''update meeting set meeting_time = ? where project_name = ?''',(e1.get(),ans))
		c.commit()
	if v4.get()==1 and v2.get()==1 and v1.get()==1:
		c.execute('''update meeting set meeting_topic = ? where project_name = ?''',(e4.get(),ans))
		c.execute('''update meeting set meeting_time = ? where project_name = ?''',(e1.get(),ans))
		c.execute('''update meeting set meeting_time = ? where project_name = ?''',(e1.get(),ans))
		c.commit()
	if v2.get()==0 and v1.get()==0 and v4.get()==0:	
		ctypes.windll.user32.MessageBoxW(0, "Select Atleast One Field", "ERROR1", 0)

def update_existing(nn,ans):
	n=Toplevel(nn)
	n.title("Enter Information")
	v1=IntVar()
	v2=IntVar()
        #v3=IntVar()
	v4=IntVar()
	c1=Checkbutton(n,text="Time",variable=v1)
	c2=Checkbutton(n,text="Date",variable=v2)
        #c3=Checkbutton(n,text="Project Name",variable=v3)
	c4=Checkbutton(n,text="Topic",variable=v4)
	e1=Entry(n)
	e2=Entry(n)
        #e3=Entry(n)
	e4=Entry(n)
	b1=Button(n,text="Update",command=lambda : change(ans,e1,e2,e4,v1,v2,v4))
	b2=Button(n,text="Back",command=lambda : back(u,n))
	c1.grid(row=1,column=0)
	c2.grid(row=2,column=0)
        #c3.grid(row=3,column=0)
	c4.grid(row=4,column=0)
	e1.grid(row=1,column=1)
	e2.grid(row=2,column=1)
        #e3.grid(row=3,column=1)
	e4.grid(row=4,column=1)
	b1.grid(row=5,column=0)
	b2.grid(row=5,column=1)
	nn.withdraw()
	n.mainloop()

def check(n,ans):
	result = c.execute("select meeting_date,meeting_time,project_name,meeting_topic from meeting where project_name = ?",(e1.get()))
	result = c.fetchall()
	if len(result)>0:
		update_existing(n,ans)
	else:
		ctypes.windll.user32.MessageBoxW(0, "Not Found", "ERROR", 0)

def old(u):
	n=Toplevel(u)
	n.title("Update Existing")
	lt1=Label(n,text="Project Name").grid(row=1,column=0)
	e1=Entry(n).grid(row=1,column=1)
        #result = c.execute("select meeting_date,meeting_time,project_name,meeting_topic from meeting where project_name = ?",(e1.get()))
        #result = c.fetchall()
        #b1=Button(n,text="Update",command=lambda : check(result,n,e1.get())).grid(row=2,column=0)
	b1=Button(n,text="Update",command=lambda : check(n,e1.get())).grid(row=2,column=0)
	b2=Button(n,text="Back",command=lambda : back(u,n)).grid(row=2,column=1)               
	u.withdraw()
	n.mainloop()
        
def update(root):
	u = Toplevel(root)
	u.title("Update")
	b1 = Button(u,text="Add New Schedule",command=lambda : new(u)).grid(row=1,column=0)
	b2 = Button(u,text="Update Old Schedule",command=lambda : old(u)).grid(row=2,column=0)
        #b3 = Button(n,text="Back",command=lambda : back(root,u)).grid(row=3,column=0)
	b3 = Button(u,text="Back",command=lambda : back(root,u)).grid(row=3,column=0)
	root.withdraw()
	u.mainloop()
