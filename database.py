import sqlite3
c = sqlite3.connect('meeting.db')

c.execute('''drop table if exists meeting''')
c.commit()

c.execute('''create table meeting (project_id integer primary key autoincrement, project_name text not null, meeting_time text, meeting_date text, meeting_topic text)''')

c.execute('''insert into meeting (project_name, meeting_time, meeting_date, meeting_topic) values ( ?,?,?,? );''',('Sachin Tendulkar','11:30','2017-10-15','Interview' ))
c.execute('''insert into meeting (project_name, meeting_time, meeting_date, meeting_topic) values ( ?,?,?,? );''',('Mustafiz','09:00','2017-10-17','Politics' ))
c.execute('''insert into meeting (project_name, meeting_time, meeting_date, meeting_topic) values ( ?,?,?,? );''',('Boss','14:30','2017-10-22','Bonus' ))
c.execute('''insert into meeting (project_name, meeting_time, meeting_date, meeting_topic) values ( ?,?,?,? );''',('Manager','13:00','2017-10-22','New Report' ))
c.execute('''insert into meeting (project_name, meeting_time, meeting_date, meeting_topic) values ( ?,?,?,? );''',('Rohit','20:30','2017-11-02','Party' ))
c.execute('''insert into meeting (project_name, meeting_time, meeting_date, meeting_topic) values ( ?,?,?,? );''',('Mitali Raj','11:00','2017-11-04','Interview' ))
c.commit()
#c.execute('''insert into meeting (project_name, meeting_time, meeting_date, meeting_topic) values ( ?,?,?,? );''',('project1','1200 hrs','30sep','meeting1'))
#c.execute('''insert into meeting (project_name, meeting_time, meeting_date, meeting_topic) values ( ?,?,?,? );''',('project2','1100 hrs','1oct','meeting2'))
#c.execute('''insert into meeting (project_name, meeting_time, meeting_date, meeting_topic) values ( ?,?,?,? );''',('project3','0900 hrs','2oct','meeting3'))
result = c.execute('''select * from meeting''')
c.commit()
for row in result:
	print(row[0],end=', ')
	print(row[1],end=', ')
	print(row[2],end=', ')
	print(row[3],end=', ')
	print(row[4])
