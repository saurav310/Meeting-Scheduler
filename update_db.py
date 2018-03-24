from tkinter import *
import sqlite3
from tkinter import messagebox
import valid

con=sqlite3.connect("meeting.db")
c=con.cursor()

def back(root,s):
	root.deiconify()
	s.destroy()

def query(m,v,root,pid,name,date,time,topic):
	if name=="" or date=="" or time=="" or topic=="":						#condition to check empty field
		messagebox.showerror("ERROR3","Each Field is Mandatory")
	else:
		if valid.checkdate(date)==False:
			messagebox.showerror("ERROR5","Date Format Error\n\tOR\nDate Value Error\nDate Format : yyyy-mm-dd")
		elif valid.checktime(time)==False:
			messagebox.showerror("ERROR6","Time Format Error\n\tOR\nTime Value Error\nTime Format : hh:mm")
		else:
			c.execute('select meeting_date,meeting_time from meeting where project_id is not '+pid)
			res=c.fetchall()
			flag=0
			for row in res:														#check if similar date and time exists	
				if row[0]==date and row[1]==time:
					flag=1
					messagebox.showerror("ERROR2","Meeting at Given \nDate and Time Already Exists")
					break
			if flag==0:															#update into DB
				c.execute('update meeting set meeting_date=?,meeting_time=?,meeting_topic=?,project_name=? where project_id=?',(date,time,topic,name,pid))
				con.commit()
				messagebox.showerror("Success","Meeting successfully updated")
				m.destroy()														#update the result
				update_db(root)													#after successful updation

def modify(a,root,v):
	#print(a)
	a=str(a)
	if a!='0':
		m=Toplevel(v)
		m.title('Meeting Scheduler')
		m.configure(background="yellow")
		l1=Label(m,font="Bold 15",fg="black",bg="yellow",text="Name :")
		l2=Label(m,font="Bold 15",fg="black",bg="yellow",text="Date  :")
		l3=Label(m,font="Bold 15",fg="black",bg="yellow",text="Time  :")
		l4=Label(m,font="Bold 15",fg="black",bg="yellow",text="Topic :")
		e1=Entry(m)
		e2=Entry(m)
		e3=Entry(m)
		e4=Entry(m)
		b1=Button(m,width=20,height=2,relief=GROOVE,text="Update",command=lambda : query(m,v,root,a,e1.get(),e2.get(),e3.get(),e4.get()))
		b2=Button(m,width=20,height=2,relief=GROOVE,text="Back",command=lambda : back(v,m))
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
		c.execute("select meeting_date,meeting_time,project_name,meeting_topic from meeting where project_id="+a)
		res=c.fetchall()
		for date,time,project,topic in res:										#fetch previous details into entry from DB
			e1.insert(0,project)
			e2.insert(0,date)
			e3.insert(0,time)
			e4.insert(0,topic)
		
		v.withdraw()
		m.mainloop()
	else:
		messagebox.showerror("ERROR4","Nothing is Selected")
		
def update_db(root):
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

	for project_id,date,time,project,topic in result:						#Show Entries in Database
		Radiobutton(v,bg="powder blue",variable=a,value=project_id).grid(row=i,column=0)		#Radiobutton assigned to each entry
		l1=Label(v,font="Bold 15",fg="black",bg="powder blue",text=date).grid(row=i,column=1)
		l2=Label(v,font="Bold 15",fg="black",bg="powder blue",text=time).grid(row=i,column=2)
		l3=Label(v,font="Bold 15",fg="black",bg="powder blue",text=project).grid(row=i,column=3)
		l4=Label(v,font="Bold 15",fg="black",bg="powder blue",text=topic).grid(row=i,column=4)
		i+=1

	b1=Button(v,width=10,height=1,relief=GROOVE,font="Bold 15",text="Update",command=lambda : modify(a.get(),root,v))
	b2=Button(v,width=10,height=1,relief=GROOVE,font="Bold 15",text="Back",command=lambda : back(root,v))
	b1.grid(row=i+1,column=1)
	b2.grid(row=i+1,column=3)
	root.withdraw()
	v.mainloop()
