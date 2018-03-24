
def checkdate(date):
	c=0
	for i in date:
		if i=='-':
			c+=1
	if c!=2:
		return False
		
	year,month,day=date.split('-')
	if len(year)!=4 or len(month)!=2 or len(day)!=2:
		return False
	try:
		year=int(year)
		month=int(month)
		day=int(day)
	except(ValueError):
		return False
		
	if month>12 or month<1:
			return False	
	if month in [1,3,5,7,8,10,12]:
		if day>31 or day<1:
			return False
	if month in [4,6,9,11]:
		if day>30 or day<1:
			return False
				
	if(year%400==0 or (year%4==0 and year%100!=0)):
		if month==2 and (day>29 or day<1):
			return False
	else:		
		if month==2 and (day>28 or day<1):
			return False
	
	return True
	
def checktime(time):
	c=0
	for i in time:
		if i==':':
			c+=1
	if c!=1:
		return False
		
	hour,min=time.split(':')
	if len(hour)!=2 or len(min)!=2:
		return False
	try:
		hour=int(hour)
		min=int(min)
	except(ValueError):
		return False
		
	if (hour<0 or hour >23) or (min<0 or min>59):
		return False
		
	return True