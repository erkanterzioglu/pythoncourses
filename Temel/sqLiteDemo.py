# -*- coding: utf-8 -*-


import sqlite3


# def selectOperasyonlari():
    
    # connection =sqlite3.connect("chinook.db")
    # cursor=connection.execute("""select FirstName,LastName
    #                   from customers
    #                   where FirstName like'%ja'   """)

# cursor=connection.execute("""select FirstName,LastName
#                           from customers
                          
#                           order by FirstName,LastName  """)


# cursor=connection.execute("""select city,count(*) from customers
#                           group by city having count(*) >1 
#                           order by count (*) desc """)



    


# for row in cursor:
#     print("First Name: " + row[0] + "\n" 
#           +"LastName: " + row[1])
#     print("**************************")


    # for row in cursor:
    #     print("City: " + str(row[0]) + "\n" 
    #       +"Count: " + str(row[1]))
    #     print("**************************")



    # connection.close()

# selectOperasyonlari()


# def insertCustomer():
#     connection=sqlite3.connect("chinook.db")
#     connection.execute("""insert into customers 
#                        (FirstName,LastName,city,email)
#                        values ('Erkan','Terzi','Izmir','erkanterzi2016@gmail.com')
#                       """ )
#     connection.commit()
#     connection.close()
    
    
    
    
# insertCustomer()

# def updateCustomer():
#     connection=sqlite3.connect("chinook.db")
#     connection.execute("""update customers set city='İstanbul' 
#                        where city='Ankara' """)
    
    
#     connection.commit()
#     connection.close()
    
# updateCustomer()



# def deleteCustomer():
#     connection=sqlite3.connect("chinook.db")
#     connection.execute("""delete from customers
#                        where city='İstanbul'
#                       """ )
#     connection.commit()
#     connection.close()

# deleteCustomer()                      

def selectOperasyonlari():
    connection=sqlite3.connect("chinook.db")
   cursor= connection.execute("""select albums.Title, artists.Name
                       from artists inner join albums
                       on artists.ArtistId =albums.ArtistId
                       """)
                       
                       
    for row in cursor:
        print("Name: "+ row[1])
        print("Title: "+ row[0])
        print("***************")
                       
                       
                       
                       
    connection.commit()
    connection.close()
    
selectOperasyonlari()