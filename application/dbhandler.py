import pg8000 
import configninja
import sys

print sys.getdefaultencoding()

conn = pg8000.connect(user=configninja.dbuser, password=configninja.dbuserpwd,database=configninja.dbname) 
t = conn.cursor()
# This is due to me using a linux based OS and my default file encoded is UTF8 as it should be
t.execute("""SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';""")
print t.fetchall()
t.close()

def addUsr(info):
	email = info['email']
	username = info['username']
	t = conn.cursor()
	t.execute('SELECT U.id FROM users U WHERE U.username = %s',(username,))
	y = t.fetchone()
	print y
	t.execute('SELECT U.id FROM users U WHERE U.email = %s',(email,))
	x = t.fetchone()
	print x
	if not y and not x:
		password = info['password']
		firstname = info['firstname']
		lastname = info['lastname']
		t.execute(
			""" INSERT INTO users(email,username,password,firstname,lastname,joinDate)
				VALUES (%s, %s, %s, %s, %s, (SELECT current_timestamp ))""",
			(email,username,password,firstname,lastname))
		conn.commit()
		#inserted new use
	else :
		#user or email already existed in the database
		return False

def verifyUser(info):
	email = info['email']
	password = info['password']
	t = conn.cursor()
	t.execute(
		'SELECT R.userName FROM users R WHERE R.email = %s AND R.password = %s',
		(email,password))
	y = t.fetchone()
	print 'y %s',y
	if not y:
		return False 
	else:
		return y
