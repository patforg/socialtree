import pg8000 
import configninja

conn = pg8000.connect(user=dbuser, password=dbuserpwd,database=dbname) 
t= conn.cursor()
t.execute("SET CLIENT_ENCODING TO 'UTF8'")
t.execute("""SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';""")
print t.fetchall()




def addUsr(info):
  print info
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
      """
      INSERT INTO user(
      userName,email,password,firstName,lastName,joinDate) 
      VALUES (%s, %s, %s, %s, %s, (SELECT current_timestamp ))""",
      (email,userName,password,name,lastname))
    conn.commit()
    #inserted new user
    return True
  else :
    #user or email already existed in the database
    return False
