import sqlite3
conn = sqlite3.connect('meeting.db')
c = conn.cursor()

c.execute('''drop table if exists meeting''')
conn.commit()

c.execute('''create table meeting (project_id int primary key not null, project_name text not null, meeting_time text, meeting_date text, meeting_topic text)''')

c.execute('''insert into meeting values ( 1,'project1','1200 hrs','30sep','meeting1' )''')
c.execute('''insert into meeting values ( 2,'project2','1100 hrs','1oct','meeting2' )''')
c.execute('''insert into meeting values ( 3,'project3','0900 hrs','2oct','meeting3' )''')
c.execute('''insert into meeting values ( 4,'project4','1500 hrs','3oct','meeting4' )''')
c.execute('''insert into meeting values ( 5,'project5','1700 hrs','4oct','meeting5' )''')
c.execute('''insert into meeting values ( 6,'project6','1000 hrs','5oct','meeting6' )''')
conn.commit()

'''result = c.execute('select * from meeting')
for row in result:
	print(row[0],end=', ')
	print(row[1],end=', ')
	print(row[2],end=', ')
	print(row[3],end=', ')
	print(row[4])
'''	

#search by project_name or meeting_time
while 1:
	n = int(input('\n1.Search by project name\n2.Search by meeting time\n3.Quit searching\n\nYour choice : '))
	if n==1:
		name = input('\nEnter project name : ')
		c.execute("select * from meeting where project_name=?",(name,))
		result = c.fetchall()
		if len(result) != 0:
			for row in result:
				print('\nID\tProject_name\tMeeting_time\tMeeting_date\tMeeting_topic')
				print(row[0],'\t',row[1],'\t',row[2],'\t',row[3],'\t\t',row[4])
		else:
			print('Project doesn\'t exist')
	elif n==2:
		time = input('\nEnter meeting time : ')
		c.execute("select * from meeting where meeting_time=?",(time,))
		result = c.fetchall()
		if len(result) != 0:
			for row in result:
				print('\nID\tProject_name\tMeeting_time\tMeeting_date\tMeeting_topic')
				print(row[0],'\t',row[1],'\t',row[2],'\t',row[3],'\t\t',row[4])
		else:
			print('No meeting found')
	else:
		print('Exitted')
		break
