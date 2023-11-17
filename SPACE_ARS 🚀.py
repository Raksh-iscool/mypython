# SPACE(ARS)🚀

# ------------------------------------------------------------------ #

import mysql.connector 
import time

# ------------------------------------------------------------------ #

connection = mysql.connector.connect(user = 'root', host = 'localhost', database = 'space_ars', passwd = '********')
ars = connection.cursor()

# ------------------------------------------------------------------ #
             
def login() :
    
    use = input('Enter your Email-ID :').strip()
    
    ars.execute('select * from accounts')
    x = ars.fetchall()
    
    for i in x :
        if i[0] == use :
            paswd = input('Enter your Password :')
            
            if paswd == i[1] :
                print('Verified')
                main()
                break
                
            else :
                for j in range(4) :
                    
                    print('Incorrect Password !')
                    print('Try again !')
                    
                    pwd = input('Enter your Password :')
                    if pwd == i[1] :
                        print('Verified !')
                        main()
                        break
                else :
                    print('Access Denied !')
                    print('5 incorrect attempts !')
                
    else :
        print('User not found !')
        
# ------------------------------------------------------------------ #        

def signup() :
    
    name = input('Enter your Name :').strip()
    no = input('Enter your Phone Number :').strip()
    
    use = name.replace(' ', '_') + no[-4::].replace(' ', '_') + '@space_ars.com'
    
    paswd = input('Enter a Password :')
    
    ars.execute('insert into accounts values("%s","%s")'%(use, paswd))
    connection.commit()
    
    print('----------------------------')
    print('Email-ID :',use)
    print('Password :',paswd)
    print('----------------------------')
    
    main()
    
# ------------------------------------------------------------------ #

def main () :

    def register():
        
        def show_seats():
            
            ars.execute('select * from seat')
            B = ars.fetchall()
            
            for i in B:
                
                for j in range(5):
                    print(i[j],end=' ')
            
                print()
        
        # ---------------------------------------------------------- #
        
        def is_vacant(R,S):
            
            ars.execute('select %s from seat where row_no = %s'%(S,R))
            X = ars.fetchone()
            
            if X[0] == 'V':
                return True
            
            else :
                return False
            
        # ---------------------------------------------------------- #    
            
        def book_seat():
            
            row = int(input('Enter the Row :'))
            seat = chr(64+int(input('Enter the Seat :')))
            
            if is_vacant(row, seat):
                
                ars.execute('update seat set %s = "X" WHERE row_no = %s'%(seat,row))
                connection.commit()
                
                print('Your Desired seat alloted !')
                print('Now Enter your details to register ::>')
                details(row,seat)
                
            else :
                
                print('Seat occupied! Choose another seat')
                book_seat()
            
        # ---------------------------------------------------------- #
        
        def details(r,s):
            
            name = input('Enter your Name :')
            age = int(input('Enter your Age :'))
            seat_no = str(r)+s
            print('Your seat number :',seat_no)
            
            ars.execute('insert into astronauts values("%s",%s,"%s",0)'%(name,age,seat_no))
            connection.commit()
         
        while True :
            print('''* --::> SPACE(ARS) Registration Menu <::-- *
                  1. Show available seats
                  2. Book a seat
                  3. Exit to Main Menu ''')
            
            ch = int(input('Enter your choice :'))
            
            if ch == 1 :
                show_seats()
                print()
                time.sleep(1.5)            
            
            elif ch == 2 :
                book_seat()
                print()
                time.sleep(1.5)
            
            else :
                break
            
    # -------------------------------------------------------------- #    
    
    def order_food():
        
        print("* --::> SPACE(ARS) Cafe' <::-- *")
        
        s = input('Enter your seat number :')
        ars.execute('select Name from astronauts where Seat_No = "%s"'%(s))
        x = ars.fetchone()
        
        if x == None :
            print('Invalid Seat Number !')
        else :
            print(x[0],', Welcome to SPACE(ARS) Cafe!', sep='')
            print()
            
            while True :
                print('--::> MENU <::--')
                ars.execute('select * from food')
                y = ars.fetchall()
                for i in y :
                    print(i[0],i[1],i[2])
                
                order = int(input('What would you like to order ?'))
                qty = int(input('How many would you take ?'))
                for i in y :
                    if i[0] == order :
                        print('You have ordered',qty,'x',i[1],'-> $',qty*i[2])
                        ars.execute('update astronauts set Total_Amount = Total_Amount + %s where Seat_No = "%s"'%(qty*i[2],s))
                        connection.commit()
                    
                z = input('Would you like to order anything else ?')
                if z[0].upper() != 'Y' :
                    print('Enjoy your Snack !')
                    print('Thank you :)')
                    break
    
    # -------------------------------------------------------------- #    
    
    def entertainment():
        
        print('--::>> Space_ARS Entertainment Zone! <<::--')
        
        s = input('Enter your seat number :')
        ars.execute('select Name from astronauts where Seat_No = "%s"'%(s))
        x = ars.fetchone()
        
        if x == None :
            print('Invalid Seat Number !')
        else :
            print(x[0],', Welcome to SPACE(ARS) Entertainment Zone!', sep='')
                
            print('~ Space_ARS honours your valuable time spent with its SpaceCraft and considers its clients getting to relax! ')
            time.sleep(5)
            print()
            print('--> Here are a list of activities you can choose to entertain yourself !')
            time.sleep(5)
                                         
            while True :                         
                ars.execute("select * from entertainment")
                o = ars.fetchall()
                print()
                
                for i in o :
                    print(i[0],' - ',i[1],' - $',i[2],sep = '')
                 
                c = int(input('Choose any activity for your Entertainment :'))
                
                for i in o:
                    if c == i[0] :
                        print('You have chosen -> ',i[1],' - $',i[2],sep = '')
                        break
                
                ars.execute('update astronauts set Total_Amount = Total_Amount + %s where Seat_No = "%s"'%(i[2],s))
                connection.commit()
                
                x = input('Would you like to choose more activities ?')
                if x.upper() != 'Y' :
                    break
                
    # -------------------------------------------------------------- #
        
    def choose_class():
        
        s = input('Enter your seat number :')
        ars.execute('select Name from astronauts where Seat_No = "%s"'%(s))
        x = ars.fetchone()
        
        if x == None :
            print('Invalid Seat Number !')
        
        else :
            
            ars.execute('select * from chosen_class')
            x = ars.fetchall()
            
            for i in x :
                if i[0] == s :
                    print('You have already opted',i[1],'Class !')
                    break
                
            else:
                        
                ars.execute('select * from class')
                x = ars.fetchall()
                for i in x:
                    print(i[0],i[1],'-> $',i[2])
                    
                c = int(input('Choose a Class for your journey :'))
                for i in x:
                    if i[0] == c :
                        
                        print('You have opted for',i[1],'class ! -> $',i[2])
                        
                        ars.execute('insert into chosen_class values("%s","%s")'%(s,i[1]))
                        connection.commit()
                        
                        ars.execute('update astronauts set Total_Amount = Total_Amount + %s where Seat_No = "%s"'%(i[2],s))
                        connection.commit()
    
    # -------------------------------------------------------------- #    
    
    def luggage():
        
        s = input('Enter your seat number :')
        ars.execute('select Name from astronauts where Seat_No = "%s"'%(s))
        x = ars.fetchone()
        
        if x == None :
            print('Invalid Seat Number !')
        else :
            ars.execute('select * from total_luggage')
            x = ars.fetchall()
            
            for i in x :
                if i[0] == s :
                    print('You have already entered your luggage !')
                    break
                
            else:
                x.append(s)
                
                ars.execute('select * from luggage')
                x = ars.fetchall()
                for i in x:
                    print(i[0],i[1],'-> $',i[2])
                    
                c = int(input('Enter your luggage Weight in kg :'))
                
                ars.execute('insert into total_luggage values("%s",%s)'%(s,c))
                connection.commit()
                
                if c < 10 and c > 0:
                    w = 1
                elif c >= 10 and c <=20 :
                    w = 2
                elif c > 20 and (c != 0 or c < 0) :
                    w = 3
                else :
                    w = 0
                
                for i in x:
                    if i[0] == w :
                        print('Your luggage is',i[1],'-> $',i[2])
                        ars.execute('update astronauts set Total_Amount = Total_Amount + %s where Seat_No = "%s"'%(i[2],s))
                        connection.commit()
        
    # -------------------------------------------------------------- #    
    
    def payment():
        
        s = input('Enter your Seat Number to proceed :')
        
        ars.execute('select * from astronauts where Seat_No = "%s"'%(s,))
        x = ars.fetchone()
        
        if x == None :
            print('Invalid Seat Number !')
            
        else :
            ars.execute('select * from payment')
            x = ars.fetchall()
            
            for i in x :
                if i[2] == s :
                    print('You have already paid the Bill !')
                    break
            
            else :
                ars.execute('select * from astronauts where Seat_No = "%s"'%(s,))
                x = ars.fetchone()
                
                ars.execute('select * from chosen_class where Seat ="%s"'%(s,))
                c = ars.fetchone()
                
                ars.execute('select * from total_luggage where Seat ="%s"'%(s,))
                w = ars.fetchone()
                
                print('****::> Check your details <::****')
                
                print()
                print('-----------------------------------')
                print()
                
                print('Name :', x[0])
                print('Age :', x[1])
                print('Class :', c[1])
                print('Luggage :', w[1],'kg')
                print('Seat Number :',x[2])
                print('Total amount to be paid* : $',x[3],sep = '')
                print('         *Includes Food Bill !')
                
                print()
                print('-----------------------------------')
                print()
                time.sleep(1.5)
                
                ch = input('Proceed to payment ?')        
                
                if ch[0].upper() == 'Y' :
                    print('''- Payment Options -
                          
                1. Google Pay ->
                2. PhonePe ->
                3. BitCoin ->
                          ''')
                  
                    c = int(input('Choose your Mode of Payment :'))
                    
                    if c == 1 :
                        print('You have chosen Google Pay !')
                        print()
                        print('Redirecting to Google Pay.....')
                        time.sleep(5)
                        print()
                        
                        print(x[0].upper())
                        print('$',x[3],' to Space_ARS !')
                        
                        y = input('Proceed to Payment ?')
                        if y[0].upper() == 'Y' :
                            print('I hereby promise to pay the bearer a sum of $',x[3],sep = '')
                            
                            ars.execute("insert into payment values('%s',%s,'%s','%s')"%(x[0],x[3],x[2],'GPay'))
                            connection.commit()
                            time.sleep(3)
                            
                            print('Transaction Successful !')
                            time.sleep(1)
                            print('Enjoy your journey!')
                        
                    elif c == 2 :
                        print('You have chosen PhonePe !')
                        print()
                        print('Redirecting to PhonePe.....')
                        time.sleep(5)
                        print()
                        
                        print(x[0].upper())
                        print('$',x[3],' to Space_ARS !')
                        
                        y = input('Proceed to Payment ?')
                        if y[0].upper() == 'Y' :
                            print('I hereby promise to pay the bearer a sum of $',x[3],sep = '')
                            
                            ars.execute("insert into payment values('%s',%s,'%s','%s')"%(x[0],x[3],x[2],'PhonePe'))
                            connection.commit()
                            time.sleep(3)
                            
                            print('Transaction Successful !')
                            time.sleep(1)
                            print('Enjoy your journey!')
                        
                    elif c == 3 :
                        print('You have chosen Bitcoin !')
                        print()
                        print('Redirecting to BitCoin.....')
                        time.sleep(5)
                        print()
                        
                        print(x[0].upper())
                        print(float(x[3])/16576.8,'Bitcoins to be paid !')
                        
                        y = input('Proceed to Payment ?')
                        if y[0].upper() == 'Y' :
                            print('I hereby promise to pay the bearer a sum of ',float(x[3])/16576.8,' BitCoins',sep = '')
                            
                            ars.execute("insert into payment values('%s',%s,'%s','%s')"%(x[0],x[3],x[2],'BitCoin'))
                            connection.commit()
                            time.sleep(3)
                            
                            print('Transaction Successful !')
                            time.sleep(1)
                            print('Enjoy your journey!')
                    
                           
    # -------------------------------------------------------------- #                
    
    def know_about_space_ars ():
        
        print('------::::>>> 🚀 SPACE(ARS)🚀 <<<::::------')
        print()
        time.sleep(2)
        
        print('--> The Space_ARS🚀  is a spacecraft manufacturer, space launch provider, and a satellite communications company founded by Arunoday, Rakshana and Samuel Ragland.')
        print()
        time.sleep(7)
        
        print("--> With the goal of reducing space transportation costs and to enable the colonization of Mars and provide real time best experience of the spacecraft and Mars, SPACE_ARS has come to it's client's service.")
        print()
        time.sleep(10)
        
        print('--> Space_ARS🚀 focuses to provide with the best space experience with the most affordable costs .')
        print()
        time.sleep(5)
        
        print('--> It provides a facile management of the booking seats and payments')
        print()
        time.sleep(5)
        
        print('--> Our motive is to make Space_ARS reach eternal heights in this arena and provide the best experience for everyone who wishes to explore the vast majorness of the space that lies above the face of the earth.')
        print()
        time.sleep(8)
        
        print('--::> Our Mission <::--')
        print()
        time.sleep(2)
        
        print('--::>>  Mars Interstellar IGNITE_7105 🚀🔥  <<::--')
        time.sleep(2)
        
        print('"It provides a 30 days to and fro voyage to Mars with the real time best experience of Mars and life in a spacecraft. Our UI is lucid and intuitive. Our space travellers can effortlessly book tickets, create and access accounts, food, entertainment, lugguage ,payment etc."')
        time.sleep(20)
    
               
    # -------------------------------------------------------------- #  
    
        
    def knowARSrules():
        
        print()
        print('  --::>>  Space_ARS Rules and Regulations  <<::--   ')
        print()
        print(' ::> Set of Rules which needs to be followed by every Denizen of this SpaceCraft ')
        print()
        print('-- GENERAL RULES --')
        time.sleep(3)
        print('   1. No Smoking is allowed in the SpaceCraft premises.')
        time.sleep(3)
        print('   2. Prohibition is to be strictly followed.')
        time.sleep(3)
        print('   3. Children under the age of 10 are not allowed.')
        time.sleep(3)
        print('   4. Wastes and used materials should be disposed properly both inside and outside the SpaceCraft.')
        time.sleep(3)
        print()
        print('-- PAYMENT RULES --')
        time.sleep(2)
        print('   1. No Cancellation of Tickets.')
        time.sleep(3)

    # ------------------------------------------------------------------ #
        
    while True :
        
        print()
        print('--::>> Space(ARS) Main menu <<::--')
        print('''
              1. Know about Space(ARS)🚀 ->
              2. Space_ARS Rules and Regulations ->
              3. Go to Registration Menu ->
              4. Go to Space(ARS) cafe ->
              5. Go to Entertainment Club ->
              6. Choose a Class ->
              7. Add your Luggage ->
              8. Proceed to Payment ->
              9. Exit
              ''')
              
        c = int(input('Enter your choice :'))
        
        if c == 1 :
            know_about_space_ars()
            time.sleep(2)
        
        elif c == 2 :
            knowARSrules()
            time.sleep(2)
            
        elif c == 3 :
            register()
            time.sleep(2)
        
        elif c == 4 :
            order_food()
            time.sleep(2)
            
        elif c == 5 :
            entertainment()
            time.sleep(2)
            
        elif c == 6 :
            choose_class()
            time.sleep(2)
            
        elif c == 7 :
            luggage()
            time.sleep(2)
                    
        elif c == 8 :
            payment()
            time.sleep(2)
        
        elif c == 9:
            break
        
        else:
            print('Invalid choice !')
            
# ------------------------------------------------------------------ #

print('------::::>>> 🚀 SPACE(ARS)🚀 <<<::::------')
time.sleep(1)

print('''
      1. Log in to your Space(ARS) account ->
      2. Sign up ( Create a new Space(ARS) account ) ->
      3. Exit Space(ARS) ->
      ''')

ch = int(input('Enter your choice :'))

if ch == 1 :
    login()
    
elif ch == 2 :
    signup()

# ------------------------------------------------------------------ #

ars.close()
connection.close()

# ------------------------------------------------------------------ #

''' # 🚀  © [ A R S ] ~ Arunoday Rakshana Samuel 🚀  # '''