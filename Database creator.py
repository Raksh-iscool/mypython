# SPACE(ARS)🚀
# ------------------------------------------------------------------ #

import mysql.connector 
connection = mysql.connector.connect(user = 'root', host = 'localhost', database = 'space_ars', passwd = '********')
ars = connection.cursor()

# ------------------------------------------------------------------ #

ars.execute('create table accounts(username varchar(50), password varchar(30))')

ars.execute('create table astronauts(Name varchar(20), Age int, Seat_No varchar(3) primary key, Total_Amount decimal(7,2) default 0.0)')

ars.execute('create table chosen_class(Seat varchar(3),Class varchar(20))')

ars.execute('create table class(S_no int, Class varchar(20), Price decimal(7,2))')

ars.execute('create table food(S_no int, Item_Name varchar(20), Rate decimal(7,2))')

ars.execute('create table luggage(S_no int, Weight varchar(20), Price decimal(7,2))')

ars.execute('create table seat(A varchar(1), B varchar(1), C varchar(1), D varchar(1), E varchar(1), row_no int)')

ars.execute('create table total_luggage(Seat varchar(3),Weight decimal(5,2))')

ars.execute('insert into class values(1,"Economy",10000)')

ars.execute('insert into class values(2,"Business",15000)')

ars.execute('insert into class values(3,"Premium",25000)')

ars.execute('insert into luggage values(1,"< 10 kg",50)')

ars.execute('insert into luggage values(2,">= 10 kg & <= 20 kg",200)')

ars.execute('insert into luggage values(3,"> 20 kg",500)')

ars.execute('insert into food values(1,"Tea",1.5)')

ars.execute('insert into food values(2,"Coffee",2)')

ars.execute('insert into food values(3,"Soft Drink",2.5)')

ars.execute('insert into food values(4,"Sandwich",3)')

ars.execute('insert into food values(5,"Dhokla",2.5)')

ars.execute('insert into food values(6,"Kachori",3)')

ars.execute('insert into food values(7,"Milk",1)')

ars.execute('insert into food values(8,"Noodles",3.5)')

ars.execute('insert into food values(9,"Pasta",3.5)')

ars.execute('insert into food values(10,"Samosa",2.5)')

ars.execute('create table payment(UserName varchar(20),AmountPaid decimal(9,2),Seat_No varchar(3),Mode_of_Payment varchar(20))')

ars.execute('create table entertainment(Sno int,Type_of_Entertainment varchar(30),Price decimal(7,2))')

ars.execute("insert into entertainment values(1,'Movies',20)")

ars.execute("insert into entertainment values(2,'FootBall',50)")

ars.execute("insert into entertainment values(3,'Cricket',30)")

ars.execute("insert into entertainment values(4,'BasketBall',40)")

ars.execute("insert into entertainment values(5,'Snooker',10)")

ars.execute("insert into entertainment values(6,'Bowling',25)")

ars.execute("insert into entertainment values(7,'Tennis',35)")

ars.execute("insert into entertainment values(8,'Zero Gravity Swimming',90)")

ars.execute("insert into entertainment values(9,'Relax Villas',40)")

ars.execute("insert into entertainment values(10,'Karaoke',20)")

ars.execute("insert into entertainment values(11,'Boxing',18)")

ars.execute("insert into entertainment values(12,'SpaceView Room',10)")

ars.execute("insert into entertainment values(13,'Chilling Bar',20)")

for i in range(1,11):
    ars.execute('insert into seat values("V", "V", "V", "V", "V", %s)'%(i,))
    
# ------------------------------------------------------------------ #

connection.commit()
ars.close()
connection.close()
print('Done !')

# ------------------------------------------------------------------ #

''' # 🚀  © [ A R S ] ~ Arunoday Rakshana Samuel 🚀  # '''