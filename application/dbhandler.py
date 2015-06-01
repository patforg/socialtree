import pg8000 
import configninja

conn = pg8000.connect(user=configninja.dbuser, 
					password=configninja.dbuserpwd,
					database=configninja.ddname) 
t= conn.cursor()
# This is due to me using a linux based OS and my default file encoded is UTF8 as it should be
t.execute("SET CLIENT_ENCODING TO 'UTF8'") 


def addUsr(info):
	email=info['email']
	userName=info['userName']
	t=conn.cursor()
	t.execute('SELECT R.userID FROM user R WHERE R.userName = %s',(userName,))
	y=t.fetchone()
	print y
	t.execute('SELECT R.userID FROM user R WHERE R.email = %s',(email,))
	x=t.fetchone()
	print x
	if not y and not x:
		password=info['password']
		name=info['firstname']
		lastname=info['lastname']
		t.execute(
		""" INSERT INTO user(
				userName,email,password,firstName,lastName,joinDate)
			VALUES (%s, %s, %s, %s, %s, (SELECT current_timestamp ))
		""",
			(email,userName,password,name,lastname))
		conn.commit()
		#inserted new user
		return True
	else :
		#user or email already existed in the database
		return False

def verifyUser(info):
	email=info['email']
	password=info['password']
	t=conn.cursor()
	t.execute(
		'SELECT R.userName FROM rater R WHERE R.email = %s AND R.password = %s',
		(email,password))
	y=t.fetchone()
	print 'y %s',y
	if not y:
		return False
	else:
		return y

