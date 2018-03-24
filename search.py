from tkinter import *
from tkinter import messagebox
import sqlite3
import valid

conn = sqlite3.connect('meeting.db')
c = conn.cursor()

def show(s,result):											#Print the Result of Queries
	if len(result)>0:
		i=2
		ans=Toplevel(s)
		#ans.minsize(380,200)
		ans.title("Meeting Scheduler")
		ans.configure(background="powder blue")
		#l=Label(ans,fg="black",bg="powder blue",font="Helvetica 25 bold",text="Result").grid(row=0,column=1)
		lt1=Label(ans,fg="brown",bg="powder blue",font="Helvetica 20 bold",text="Date").grid(row=1,column=0)
		lt2=Label(ans,fg="brown",bg="powder blue",font="Helvetica 20 bold",text="Time").grid(row=1,column=1)
		lt3=Label(ans,fg="brown",bg="powder blue",font="Helvetica 20 bold",text="Name").grid(row=1,column=2)
		lt4=Label(ans,fg="brown",bg="powder blue",font="Helvetica 20 bold",text="Topic").grid(row=1,column=3)
		color=["red","yellow"]
		j=0
		for date,time,project,topic in result:
			l1=Label(ans,height=1,width=15,font="Bold 15",fg="black",bg=color[j],text=date).grid(row=i,column=0)
			l2=Label(ans,height=1,width=15,font="Bold 15",fg="black",bg=color[j],text=time).grid(row=i,column=1)
			l3=Label(ans,height=1,width=15,font="Bold 15",fg="black",bg=color[j],text=project).grid(row=i,column=2)
			l4=Label(ans,height=1,width=15,font="Bold 15",fg="black",bg=color[j],text=topic).grid(row=i,column=3)
			i+=1
			if j==1:
				j=0
			else:
				j=1
		b1=Button(ans,width=10,height=1,relief=GROOVE,font="Bold 15",text="Back",command=lambda : back(s,ans)).grid(row=i+1,column=1)
		i1=Label(ans,width=20,height=1,bg="powder blue",text="").grid(row=i+1,column=0)
		i2=Label(ans,width=20,height=1,bg="powder blue",text="").grid(row=i+1,column=2)
		i3=Label(ans,width=20,height=1,bg="powder blue",text="").grid(row=i+1,column=3)
		s.withdraw()
		ans.mainloop()
	else:																			#If No Result is Obtained Show Dialog Box
		messagebox.showerror("ERROR0","Not Found")

def do(s,e1,e2,v1=1,v2=1):					#Enter Possible Queries in this Function
	if v1.get()==1 and v2.get()==0:							#Condition for Search by Name
		result = c.execute("select meeting_date,meeting_time,project_name,meeting_topic from meeting where project_name like '"+e1.get()+"%' or project_name like '"+e1.get().lower()+"%' or project_name like '"+e1.get().upper()+"%'order by date(meeting_date),time(meeting_time);")
		result = c.fetchall()
		show(s,result)
		
	if v2.get()==1 and v1.get()==0:							#Condition for Search by Date
		if valid.checkdate(e2.get())==False:
			messagebox.showerror("ERROR5","Date Format Error\n\tOR\nDate Value Error\nDate Format : yyyy-mm-dd")
		else:
			result = c.execute("select meeting_date,meeting_time,project_name,meeting_topic from meeting where meeting_date='"+e2.get()+"' order by date(meeting_date),time(meeting_time);")
			result = c.fetchall()
			show(s,result)
		
	if v2.get()==1 and v1.get()==1:								#Condition for Search by Both Name and User
		if valid.checkdate(e2.get())==False:
			messagebox.showerror("ERROR5","Date Format Error\n\tOR\nDate Value Error\nDate Format : yyyy-mm-dd")
		else:	
			result = c.execute("select meeting_date,meeting_time,project_name,meeting_topic from meeting where meeting_date='"+e2.get()+"' and project_name='"+e1.get()+"' order by date(meeting_date),time(meeting_time);")
			result = c.fetchall()
			show(s,result)
		
	if v2.get()==0 and v1.get()==0:								#IF no fields are selected
		messagebox.showerror("ERROR1","No Fields Selected")

def back(root,s):
	root.deiconify()
	s.destroy()
	
def search(root):
	s=Toplevel(root)
	s.title("Meeting Scheduler")
	v1=IntVar()
	v2=IntVar()
	s.minsize(300,130)
	s.configure(background="light green")
	#l1=Label(s,text="Search Form")
	c1=Checkbutton(s,font="Bold 15",fg="black",bg="light green",text="Name :",variable=v1)
	c2=Checkbutton(s,font="Bold 15",fg="black",bg="light green",text="Date  :",variable=v2)
	e1=Entry(s,width=31)
	e2=Entry(s,width=31)
	b1=Button(s,width=20,height=2,relief=GROOVE,text="Search",command=lambda : do(s,e1,e2,v1,v2))
	b2=Button(s,width=20,height=2,relief=GROOVE,text="Back",command=lambda : back(root,s))
	#l1.grid(row=0,column=1)
	c1.grid(row=1,column=0)
	c2.grid(row=2,column=0)
	e1.grid(row=1,column=1)
	e2.grid(row=2,column=1)
	#b1.grid(row=3,column=0)
	#b2.grid(row=3,column=1)
	b1.place(x=0,y=80)
	b2.place(x=150,y=80)
	root.withdraw()
	s.mainloop()