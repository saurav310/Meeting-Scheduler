from tkinter import *
import sqlite3

def back(root,s):
	root.deiconify()
	s.destroy()
	
def view(root):
	i=2
	con=sqlite3.connect("meeting.db")
	result = con.execute('''select meeting_date,meeting_time,project_name,meeting_topic from meeting order by date(meeting_date),time(meeting_time)''')
	v=Toplevel(root)
	v.title("Meeting Scheduler")
	v.minsize(380,200)
	v.configure(background="powder blue")
	
	#l=Label(v,text="Show Schedule")
	lt1=Label(v,fg="brown",bg="powder blue",font="Helvetica 20 bold",text=" Date ").grid(row=1,column=0)
	lt2=Label(v,fg="brown",bg="powder blue",font="Helvetica 20 bold",text=" Time ").grid(row=1,column=1)
	lt3=Label(v,fg="brown",bg="powder blue",font="Helvetica 20 bold",text=" Name ").grid(row=1,column=2)
	lt4=Label(v,fg="brown",bg="powder blue",font="Helvetica 20 bold",text=" Topic ").grid(row=1,column=3)
	color=["yellow","red"]
	j=0
	for date,time,project,topic in result:
		l1=Label(v,height=1,width=15,font="Bold 15",fg="black",bg=color[j],text=date).grid(row=i,column=0)
		l2=Label(v,height=1,width=15,font="Bold 15",fg="black",bg=color[j],text=time).grid(row=i,column=1)
		l3=Label(v,height=1,width=15,font="Bold 15",fg="black",bg=color[j],text=project).grid(row=i,column=2)
		l4=Label(v,height=1,width=15,font="Bold 15",fg="black",bg=color[j],text=topic).grid(row=i,column=3)
		i+=1
		if j==1:
			j=0
		else:
			j=1
	b1=Button(v,compound=LEFT,width=10,height=1,relief=GROOVE,text="Back",font="Bold 15",command=lambda : back(root,v))
	i1=Label(v,width=10,height=1,bg="powder blue",text="").grid(row=i+1,column=0)
	i2=Label(v,width=10,height=1,bg="powder blue",text="").grid(row=i+1,column=2)
	i3=Label(v,width=10,height=1,bg="powder blue",text="").grid(row=i+1,column=3)
	#l.grid(row=0,column=1)
	#t1.pack()
	b1.grid(row=i+1,column=1)
	#b1.place(anchor=S)
	root.withdraw()
	v.mainloop()
	#root.destroy()