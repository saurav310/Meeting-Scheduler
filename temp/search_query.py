import sqlite3
conn = sqlite3.connect('meeting.db')
c = conn.cursor()

#search by project_name or meeting_date
while 1:
	n = int(input('\n1.Search by project name\n2.Search by meeting date\n3.Quit searching\n\nYour choice : '))
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
		time = input('\nEnter meeting date : ')
		c.execute("select * from meeting where meeting_date=?",(time,))
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
