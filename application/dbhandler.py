import pg8000 


conn = pg8000.connect(user="postgres", password="")  

print conn 