
    try:
        from prettytable import PrettyTable
    except ImportError:
        from os import system as sys
        sys("pip install prettytable && exit")
        del sys

    import mysql
    import mysql.connector
    from mysql.connector import errorcode
    import os

    x=PrettyTable()
    x.field_names = ["Item Number", "Item Name", "Manufacturer", "Price", "Quantity", "Date Of Upload"]

    try:
        os.system('cls')
        obj=mysql.connector.connect(user='root',password='tiger',host='localhost',database='scamazon',autocommit=True)
        cur=obj.cursor()
        qry=("select * from itemrecord")
        cur.execute(qry)
        data=cur.fetchall()
        for t in data:
            x.add_row([t[0],t[1],t[2],t[3],t[4],t[5]])
                
        #for (Ino,Iname,Manu,Price,QTY,DOP) in cur:
               
        
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Incorrect Username or Password!!")
        elif err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Database Does Not Exist")
        else:
            print(err)
    else:
        obj.close()
    print(x)
