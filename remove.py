from tkinter import *
import sqlite3
from tkinter import messagebox

con=sqlite3.connect("meeting.db")

def back(root,s):
	root.deiconify()
	s.destroy()

def delete(a,root,v):
	#print(a)
	a=str(a)
	if a!='0':
		con.execute("delete from meeting where project_id ="+a)
		con.commit()
		messagebox.showerror("Success","Succesfully Deleted")
		v.destroy()								#Update the Result 
		remove(root)							#after delete operation
	else:
		messagebox.showerror("ERROR4","Nothing is Selected")
		
def remove(root):
	i=2
	a=IntVar()
	result = con.execute('''select project_id,meeting_date,meeting_time,project_name,meeting_topic from meeting order by date(meeting_date),time(meeting_time)''')
	
	v=Toplevel(root)
	v.title("Meeting Scheduler")
	v.configure(background="powder blue")
	lt1=Label(v,fg="brown",bg="powder blue",font="Helvetica 20 bold",text="Date").grid(row=1,column=1)
	lt2=Label(v,fg="brown",bg="powder blue",font="Helvetica 20 bold",text="Time").grid(row=1,column=2)
	lt3=Label(v,fg="brown",bg="powder blue",font="Helvetica 20 bold",text="Name").grid(row=1,column=3)
	lt4=Label(v,fg="brown",bg="powder blue",font="Helvetica 20 bold",text="Topic").grid(row=1,column=4)

	for project_id,date,time,project,topic in result:					#Show Entries in Database
		Radiobutton(v,bg="powder blue",variable=a,value=project_id).grid(row=i,column=0)	#Radiobutton assigned to each entry
		l1=Label(v,font="Bold 15",fg="black",bg="powder blue",text=date).grid(row=i,column=1)
		l2=Label(v,font="Bold 15",fg="black",bg="powder blue",text=time).grid(row=i,column=2)
		l3=Label(v,font="Bold 15",fg="black",bg="powder blue",text=project).grid(row=i,column=3)
		l4=Label(v,font="Bold 15",fg="black",bg="powder blue",text=topic).grid(row=i,column=4)
		i+=1

	b1=Button(v,width=10,height=1,relief=GROOVE,font="Bold 15",text="Delete",command=lambda : delete(a.get(),root,v))
	b2=Button(v,width=10,height=1,relief=GROOVE,font="Bold 15",text="Back",command=lambda : back(root,v))
	b1.grid(row=i+1,column=1)
	b2.grid(row=i+1,column=3)
	root.withdraw()
	v.mainloop()