import sqlite3
from tkinter import messagebox
from tkinter import *
import valid

con = sqlite3.connect('meeting.db')

def back(root,s):
	root.deiconify()
	s.destroy()

def add(u):
	def store():
		flag=False
		if e1.get()=="" or e2.get()=="" or e3.get()=="" or e4.get()=="":				#Condition to check Empty Fields
			messagebox.showerror("ERROR3","Each Field is Mandatory")
		else:
			if valid.checkdate(e2.get())==False:
				messagebox.showerror("ERROR5","Date Format Error\n\tOR\nDate Value Error\nDate Format : yyyy-mm-dd")
				n.wait_window()
			elif valid.checktime(e3.get())==False:
				messagebox.showerror("ERROR6","Time Format Error\n\tOR\nTime Value Error\nTime Format : hh:mm")
				n.wait_window()
			else:
				c = con.cursor()
				c.execute('''select meeting_date,meeting_time from meeting''')				#Fetch Date and Time from DB
				res=c.fetchall()
				for row in res:																#Check if Similar Date and Time Exists
					if row[0]==e2.get() and row[1]==e3.get():
						flag=True
						messagebox.showerror("ERROR2","Meeting at Given \nDate and Time Already Exists")
						n.wait_window()
						break
						
				if flag==False:																#Add New Entry to Database
					c.execute('''insert into meeting (project_name, meeting_time, meeting_date, meeting_topic) values ( ?,?,?,? )''',(e1.get(),e3.get(),e2.get(),e4.get()))
					messagebox.showerror("Success","Succesfully Added")
					n.wait_window()
					con.commit()
					n.destroy()
					u.deiconify()
		
	n=Toplevel(u)
	n.title("Meeting Scheduler")
	n.configure(background="light blue")
	l1=Label(n,font="Bold 15",fg="black",bg="light blue",text="Name : ")
	l2=Label(n,font="Bold 15",fg="black",bg="light blue",text="Date  : ")
	l3=Label(n,font="Bold 15",fg="black",bg="light blue",text="Time  : ")
	l4=Label(n,font="Bold 15",fg="black",bg="light blue",text="Topic : ")
	e1=Entry(n)
	e2=Entry(n)
	e3=Entry(n)
	e4=Entry(n)
	b1=Button(n,width=20,height=2,relief=GROOVE,text="Add",command=store)
	b2=Button(n,width=20,height=2,relief=GROOVE,text="Back",command=lambda : back(u,n))
	l1.grid(row=1,column=0)
	l2.grid(row=2,column=0)
	l3.grid(row=3,column=0)
	l4.grid(row=4,column=0)
	e1.grid(row=1,column=1)
	e2.grid(row=2,column=1)
	e3.grid(row=3,column=1)
	e4.grid(row=4,column=1)
	b1.grid(row=5,column=0)
	b2.grid(row=5,column=1)
	u.withdraw()
	n.mainloop()