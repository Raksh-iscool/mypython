import mysql.connector as mysql
import datetime

db = mysql.connect(host = 'localhost',user='root',password = '123456',database = 'aksay')
c = db.cursor()


def User(name,email,password):
    script = f'INSERT INTO users(name,email,password) VALUES("{name}","{email}","{password}");'
    c.execute(script)
    db.commit()
    print('done')

def login(user,password):
    print(user,password)
    c.execute(f'SELECT name, password FROM users WHERE name = "{user}" AND password = "{password}";')
    data = c.fetchall()
    
    if data:
        date,time = str(datetime.datetime.today()).split()
        c.execute(f'INSERT INTO log VALUES("{user}","{date}","{time}");')
        db.commit()
        print('Logined in')
    else:
        print('Invaild username or password')

