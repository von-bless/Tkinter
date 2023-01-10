#user interaction;
from tkinter import *
from tkinter import ttk
import datetime
from PIL import ImageTk,Image


#PYTHON MODULE MEMBER
from mysql.connector import errorcode
from mysql.connector import (connection)
import os

root=Tk()#page1
root.title("SCAMAZON")
root.configure(bg='burlywood4')
root.iconbitmap(r'd:\python\scam.ico')

def display():
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

    
def BUY1():
   
    from mysql.connector import errorcode
    from datetime import date
    import mysql
    from mysql.connector import (connection)
    import os

    

    def destroy1():
        screen1.destroy()

    def destroy2():
        screen2.destroy()

    
        
        

    def buy():
        
        global ino
        global mno
        global price
        global qty
        global screen1
        screen1=Toplevel(rot)
        screen1.geometry("500x500")
        screen1.title("Buy What You May")
        screen1.configure(bg = "thistle")
        screen1.iconbitmap(r'd:\python\scam.ico')   
        ino = StringVar()
        mno = StringVar()
        price = IntVar()
        qty = IntVar()
        def submit():
            try:
                os.system('cls')
                obj=connection.MySQLConnection(user='root',password='tiger',host='localhost',database='scamazon',autocommit=True)
                cur=obj.cursor()
                
                
                qry=("insert into cart values('{}','{}',{},{})".format(a.get(),b.get(),int(c.get()),int(d.get())))
                cur.execute(qry)
                obj.commit()
                cur.close()
                obj.close()
                Label(text = "Successfully Added to Cart!!!", fg = "green")
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_BAD_DB_ERROR:
                    print("Incorrect Username or Password!!")
                elif err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print("Database Does Not Exist")
                else:
                    print(err)
            else:
                obj.close()
        
        Label(screen1, text = "BUY", bg = "sky blue", width = "300", height = "2", font = ("Calibri", 13)).pack()

        Label(screen1, text = "Please Enter Details Below:",bg = "thistle", font = ("Calibri", 13)).pack()
        Label(screen1, text = "",bg = "thistle").pack()
        Label(screen1, text = "Item Code * ",bg = "thistle").pack()
        a=Entry(screen1)
        a.pack()
        Label(screen1, text = "", bg = "thistle").pack()

        Label(screen1, text = "Member Code * ",bg = "thistle").pack()
        b=Entry(screen1)
        b.pack()
        Label(screen1, text = "", bg = "thistle").pack()

        Label(screen1, text = "Price * ",bg = "thistle").pack()
        c=Entry(screen1)
        c.pack()
        Label(screen1, text = "", bg = "thistle").pack()

        Label(screen1, text = "Quantity * ",bg = "thistle").pack()
        d=Entry(screen1)
        d.pack()
        
        Label(screen1, text = "", bg = "thistle").pack()
        Button(screen1, text = "SUBMIT", height = "2", width = "30", command = submit).pack()
        
        Label(screen1, text = "", bg = "thistle").pack()
        Button(screen1, text = "BACK", height = "2", width = "30", command = destroy1).pack()
        
        screen1.mainloop()

        
    #-----------------------------------------------------------------------------------------------------------------------

    def cart():
        global screen2
        try:
            os.system('cls')
            obj=connection.MySQLConnection(user='root',password='tiger',host='localhost',database='scamazon',autocommit=True)
            cur=obj.cursor()
            screen2=Toplevel(rot)
            screen2.configure(bg = "thistle")
            screen2.iconbitmap(r'd:\python\scam.ico')
            screen2.geometry("400x800")
            screen2.title("Your Cart")
            qry1=("select count(*) from cart")
            qry2=("select I.Ino,Manu,Iname,M.Mno,Mname,DOP from itemrecord I,`member` M,cart C where I.Ino=C.Ino and C.Mno=M.Mno")
            cur.execute(qry1)
            data=cur.fetchall()

            Label(screen2, text = "CART", bg = "red", width = "300", height = "2", font = ("Calibri", 13)).pack()

            Label(screen2, text = "",bg = "thistle").pack()
            for x in data:
                if x[0]==0:
                    Label(screen2, text = "Your Cart is Empty...",bg = "thistle", font = ("Calibri", 13)).pack()
                else:
                    cur.execute(qry2)
                    Label(screen2, text = "Here Is Your Cart",bg = "thistle", font = ("Calibri", 13)).pack()
                    Label(screen2, text = "", bg = "thistle").pack()
                    
                    for (Ino,Manu,Iname,Mno,Mname,DOP) in cur:
                        Label(screen2, text = "Item Code:",bg = "thistle", font = ("Calibri", 13)).pack()
                        Label(screen2, text = Ino,bg = "thistle").pack()
                        
                        Label(screen2, text = "Manufacturer:",bg = "thistle", font = ("Calibri", 13)).pack()
                        Label(screen2, text = Manu,bg = "thistle").pack()
                        
                        Label(screen2, text = "Item Name:",bg = "thistle", font = ("Calibri", 13)).pack()
                        Label(screen2, text = Iname,bg = "thistle").pack()
                        
                        Label(screen2, text = "Member Number:",bg = "thistle", font = ("Calibri", 13)).pack()
                        Label(screen2, text = Mno,bg = "thistle").pack()
                        
                        Label(screen2, text = "Member Name",bg = "thistle", font = ("Calibri", 13)).pack()
                        Label(screen2, text = Mname,bg = "thistle").pack()

                        Label(screen2, text = "Date of Manufacture",bg = "thistle", font = ("Calibri", 13)).pack()
                        Label(screen2, text = DOP,bg = "thistle").pack()

                        Label(screen2, text = "", bg = "thistle").pack()
                        
                    cur.close()
                    obj.close()
            Button(screen2, text = "Back", height = "2", width = "30", command = destroy2, bg = "sienna1").pack()
                    
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Incorrect Username or Password!!")
            elif err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Database Does Not Exist")
            else:
                print(err)
        else:
            obj.close()
            
        root.mainloop()

    #-----------------------------------------------------------------------------------------------------------------------

    rot=Tk()
    rot.geometry("300x300")
    rot.title("YOUR CHOICE")
    rot.configure(bg = "thistle")
    rot.iconbitmap(r'd:\python\scam.ico')

    Label(rot, text = "SCAMAZON", bg = "light green", width = "300", height = "2", font = ("Calibri", 15)).pack()
    Label(rot, text = "",bg = "thistle").pack()

    Button(rot, text = "MART", height = "2", width = "30", command = display, bg = "sienna1").pack()
    Label(rot, text = "",bg = "thistle").pack()

    Button(rot, text = "BUY", height = "2", width = "30", command = buy, bg = "sienna1").pack()
    Label(rot, text = "",bg = "thistle").pack()

    Button(rot, text = "YOUR CART", height = "2", width = "30", command = cart, bg = "sienna1").pack()
    Label(rot, text = "",bg = "thistle").pack()

    Button(rot, text = "BACK", height = "2", width = "30", command = rot.destroy, bg = "sienna1").pack()

    rot.mainloop()
    #################################################################################################################

def sell():
    def REGISTER():
        import mysql.connector
        try:    
            cnx=mysql.connector.connect(user='root',password="tiger",host="localhost",database="SCAMAZON")
            cur=cnx.cursor()
            q="select * from Itemrecord"
            cur.execute(q)
            p=cur.fetchall()
            Ino="I000"+str(cur.rowcount+1)
            date=datetime.date(int(YYYY_.get()),int(MM_.get()),int(DD_.get()))
            s="insert into Itemrecord values('{}','{}','{}','{}','{}','{}')".format(Ino,Iname_.get(),Manufacturer_.get(),int(Price_.get()),int(QTY_.get()),date)
            cur.execute(s)
            print("SUCCESSFULLY UPLOADED ITEM DETAILS WAITING FOR SHIPMENT")
            print("YOUR ITEM NUMBER IS ",Ino)
            cnx.commit()
            top4=Toplevel()
            top4.geometry("300x300")
            top4.iconbitmap(r'd:/python/scam.ico')
            top4.configure(bg='thistle')
            top4.title("WAIT FOR IT TO GET SOLD")

            #DIALOGUE BOX
            comment=Label(top4,text="WHAT WOULD YOU LIKE TO DO NOW",bg='black',foreground='white')
            comment.grid(row=0,column=0,padx=20,pady=20,columnspan=2)
            #buttons for final encounter
            CLOSE=Button(top4,text="BACK",command=top4.destroy,bg='skyblue',foreground='red')
            CLOSE.grid(row=1,column=0,padx=20,pady=20)

            BUY=Button(top4,text="IF YOU WANT TO BUY",command=BUY1,bg='skyblue',foreground='red')
            BUY.grid(row=1,column=1,padx=20,pady=20)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("SOMETHING IS WRONG WITH YOUR USER NAME OR PASSWORD")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("DATABASE DOES NOT EXIST")
            else:
                print(err)
        else:
            cnx.close()   
    #creating text lables
    
    top3=Toplevel()
    top3.geometry("600x600")
    top3.title("SELLING ON GOING")
    top3.iconbitmap(r'd:/python/scam.ico')
    top3.configure(bg='DarkOrange1')
    intro=Label(top3,text="ENTER THE DETAILS OF YOUR ITEMS BELOW",bg='DarkOrange1')
    intro.grid(row=0,column=0,columnspan=2)
    #CREATING TEXT BOXES

    Iname_=Entry(top3,width=30,bg="skyblue")
    Iname_.grid(row=1,column=1,padx=20,pady=20,columnspan=20)
    
    Manufacturer_=Entry(top3,width=30,bg="skyblue")
    Manufacturer_.grid(row=2,column=1,padx=20,pady=20,columnspan=20)

    Price_=Entry(top3,width=30,bg="skyblue")
    Price_.grid(row=3,column=1,padx=20,pady=20,columnspan=20)

    QTY_=Entry(top3,width=30,bg="skyblue")
    QTY_.grid(row=4,column=1,padx=20,pady=20,columnspan=20)

    #for date
    YYYY_=Entry(top3,width=30,bg="skyblue")
    YYYY_.grid(row=5,column=1,padx=20,pady=20,columnspan=20)
    MM_=Entry(top3,width=30,bg="skyblue")
    MM_.grid(row=6,column=1,padx=20,pady=20,columnspan=20)
    DD_=Entry(top3,width=30,bg="skyblue")
    DD_.grid(row=7,column=1,padx=20,pady=20,columnspan=20)

    #apponting names to text boxes

    Inmae_label=Label(top3,text="ENTER ITEM NAME WITH DETAILS",bg='DarkOrange1')
    Inmae_label.grid(row=1,column=0,padx=20,pady=20)

    Manufacturer_label=Label(top3,text="MANUFACTURER NAME",bg='DarkOrange1')
    Manufacturer_label.grid(row=2,column=0,padx=20,pady=20)

    Price_label=Label(top3,text="PRICE OF EACH",bg='DarkOrange1')
    Price_label.grid(row=3,column=0,padx=20,pady=20)

    QTY_label=Label(top3,text="QUANTITY",bg='DarkOrange1')
    QTY_label.grid(row=4,column=0,padx=20,pady=20)

    YYYY_label=Label(top3,text="YEAR OF PURCHASE",bg='DarkOrange1')
    YYYY_label.grid(row=5,column=0,padx=20,pady=20)
    MM_label=Label(top3,text="MONTH OF PURCHAE ",bg='DarkOrange1')
    MM_label.grid(row=6,column=0,padx=20,pady=20)
    DD_label=Label(top3,text="DAY OF PURCHASE",bg='DarkOrange1')
    DD_label.grid(row=7,column=0,padx=20,pady=20)

    #DEFINNING SUBMIT BUTTON
    submit1_=Button(top3,text="SUBMIT",command=REGISTER,foreground="yellow",bg="purple")
    submit1_.grid(row=8,column=1,padx=40,pady=20,ipadx=10)

    submit2_=Button(top3,text="BACK",command=top3.destroy,foreground="yellow",bg="purple")
    submit2_.grid(row=9,column=1,padx=40,pady=20,ipadx=10)

def Login():#buy or sell
    top1=Toplevel()#page3
    top1.geometry("400x200")
    top1.iconbitmap(r'd:\python\scam.ico')
    top1.configure(bg='hot pink')
    import mysql.connector
    cnx=mysql.connector.connect(user='root',password="tiger",host="localhost",database="SCAMAZON")
    cur=cnx.cursor()
    Mno_=Entry(top1,width=30,bg='skyblue')
    Mno_.grid(row=0,column=1,padx=20)

    PASSWORD_=Entry(top1,width=30,bg='skyblue',show='*')
    PASSWORD_.grid(row=1,column=1,padx=20)
    
    def submit2():
        try:
            s1="select * from MEMBER natural join PASSWORD"
            cur.execute(s1)
            data=cur.fetchall()
            for x in data:
                if x[0]==Mno_.get() and x[5]==int(PASSWORD_.get()):
                    s="select*from Member natural join Itemrecord"
                    cur.execute(s)
                    

                    top2=Toplevel()#after login
                    top2.geometry("300x200")
                    top2.title("BUY OR SELL") 
                    top2.configure(bg='hot pink')       

                    #CREATING TEXT labels
                    WELCOME=Label(top2,text="HI CHOOSE THE BELOW OPTIONS",bg='hot pink',foreground='white')
                    WELCOME.grid(row=0,column=0,columnspan=2)
                    
                    buy=Button(top2,text="BUY",padx=40,pady=20,command=BUY1,bg="skyblue",foreground='red')
                    buy.grid(row=2,column=0)
                    
                    sell_=Button(top2,text="SELL",padx=40,pady=20,command=sell,bg="yellow",foreground="purple")
                    sell_.grid(row=2,column=1)


                    exit_=Button(top2,text="BACK",padx=40,pady=20,command=top2.destroy,bg="red",foreground="green")
                    exit_.grid(row=3,column=0)

                    update_=Button(top2,text="UPDATE",padx=40,pady=20,command=UPDATE,bg="green",foreground="black")
                    update_.grid(row=3,column=1)
       
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("SOMETHING IS WRONG WITH YOUR USER NAME OR PASSWORD")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("DATABASE DOES NOT EXIST")
            else:
                print(err)
        else:
            cnx.close()

    #CREATING TEXT LABLES
    Mno_label=Label(top1,text="ENTER MEMBER NUMBER",foreground='blue',bg='hot pink')
    Mno_label.grid(row=0,column=0)
    PASSWORD_label=Label(top1,text="ENTER PASSWORD",foreground='blue',bg='hot pink')
    PASSWORD_label.grid(row=1,column=0) 

    #creating submit button
    button_4=Button(top1,text="SUBMIT",padx=40,pady=20,command=submit2,bg="purple",foreground="yellow")
    button_4.grid(row=3,column=0)
    import mysql.connector
    
    button_5=Button(top1,text="BACK",padx=40,pady=20,command=top1.destroy,bg="purple",foreground="yellow")
    button_5.grid(row=3,column=1)
    def update1():
        
        new=Toplevel()
        new.geometry("200x200")
        new.configure(bg='hot pink')
        new.iconbitmap(r'd:\python\scam.ico')
        new.title("CHANGE MEMBER NAME")
        new_1=Entry(new,width=30,bg='skyblue')
        new_1.grid(row=0,column=1)
        new_label=Label(new,text="ENTER NEW NAME",bg='hot pink')
        new_label.grid(row=0,column=0,padx=40,pady=20)
        #print(new_1.get())
        def exe1():
            cnx=mysql.connector.connect(user='root',password="tiger",host="localhost",database="SCAMAZON",autocommit=True)
            cur=cnx.cursor()
            s="update Member set Mname='{}' where Mno='{}'".format(new_1.get(),Mno_.get())
            cur.execute(s)
            cnx.commit()
            print("UPDATED SUCCESSFULLY!")
        new_submit=Button(new,text="SUBMIT",command=exe1,bg="yellow")
        
        #print(new_1.get(),"ttt")
        new_submit.grid(row=1,column=0)
        new_back=Button(new,text="BACK",command=new.destroy,bg='yellow')
        BACK=Button(new,text="BACK",command=new.destroy,bg='yellow')
        BACK.grid(row=1,column=1)
        #print("DONE")

    def update2():
        cnx=mysql.connector.connect(user='root',password="tiger",host="localhost",database="SCAMAZON",autocommit=True)
        cur=cnx.cursor()
        new1=Toplevel()
        new1.configure(bg="hot pink")
        new1.geometry("400x200")
        new1.iconbitmap(r'd:\python\scam.ico')
        new1.title("CHANGE PHONE NUMBER")
        new1_=Entry(new1,width=30,bg="skyblue")
        new1_.grid(row=0,column=1)
        new1_label=Label(new1,text="ENTER NEW PHONE NUMBER",bg="hot pink")
        new1_label.grid(row=0,column=0,padx=40,pady=20)
        def exe2():
            cnx=mysql.connector.connect(user='root',password="tiger",host="localhost",database="SCAMAZON",autocommit=True)
            cur=cnx.cursor()
            s="update Member set MOB={} where Mno='{}'".format(int(new1_.get()),Mno_.get())
            cur.execute(s)
            cnx.commit()
            print("UPDATED SUCCESSFULLY!")
        new1_submit=Button(new1,text="SUBMIT",command=exe2,bg='yellow')
        new1_submit.grid(row=1,column=0)
        BACK=Button(new1,text="BACK",command=new1.destroy,bg='yellow')
        BACK.grid(row=1,column=1)
        
    def update3():
        cnx=mysql.connector.connect(user='root',password="tiger",host="localhost",database="SCAMAZON",autocommit=True)
        cur=cnx.cursor()
        new2=Toplevel()
        new2.geometry("400x200")
        new2.configure(bg='hot pink')
        new2.title("CHANGE ADDRESS ")
        new2.iconbitmap(r'd:\python\scam.ico')
        new2_=Entry(new2,width=30,bg='skyblue')
        new2_.grid(row=0,column=1)
        new2_label=Label(new2,text="ENTER NEW ADDRESS",bg='hot pink')
        new2_label.grid(row=0,column=0,padx=40,pady=20)
        def exe3():
            cnx=mysql.connector.connect(user='root',password="tiger",host="localhost",database="SCAMAZON",autocommit=True)
            cur=cnx.cursor()
            s="update Member set ADR='{}' where Mno='{}'".format(new2_.get(),Mno_.get())
            cur.execute(s)
            cnx.commit()
            print("UPDATED SUCCESSFULLY!")
        new2_submit=Button(new2,text="SUBMIT",command=exe3,bg='yellow')
        new2_submit.grid(row=1,column=0)
        BACK=Button(new2,text="BACK",command=new2.destroy,bg='yellow')
        BACK.grid(row=1,column=1)
        print("DONE") 
    def update4():
        cnx=mysql.connector.connect(user='root',password="tiger",host="localhost",database="SCAMAZON",autocommit=True)
        cur=cnx.cursor()
        new3=Toplevel()
        new3.iconbitmap(r'd:\python\scam.ico')
        new3.geometry("500x400")
        new3.title("CHANGE MULTIPLE")
        new3.configure(bg='hot pink')
        new3_=Entry(new3,width=30,bg='skyblue')
        new3_.grid(row=0,column=1)
        new3_label=Label(new3,text="ENTER NEW NAME",bg='hot pink')
        new3_label.grid(row=0,column=0,padx=40,pady=20)
        
        new31_=Entry(new3,width=30,bg='skyblue')
        new31_.grid(row=1,column=1,padx=40,pady=20)
        new31_label=Label(new3,text="ENTER NEW MOBILE NUMBER",bg='hot pink')
        new31_label.grid(row=1,column=0,padx=40,pady=20)

        new32_=Entry(new3,width=30,bg='skyblue')
        new32_.grid(row=2,column=1,padx=40,pady=20)
        new32_label=Label(new3,text="ENTER NEW ADDRESS",bg='hot pink')
        new32_label.grid(row=2,column=0,padx=40,pady=20)
        def give3():
            cnx=mysql.connector.connect(user='root',password="tiger",host="localhost",database="SCAMAZON",autocommit=True)
            cur=cnx.cursor()
            s1="update Member set Mname='{}' where Mno='{}'".format(new3_.get(),Mno_.get())
            s2="update Member set MOB={} where Mno='{}'".format(int(new31_.get()),Mno_.get())
            s3="update Member set ADR='{}' where Mno='{}'".format(new32_.get(),Mno_.get())
            cur.execute(s1)
            cur.execute(s2)
            cur.execute(s3)
            cnx.commit()

        new3_submit=Button(new3,text="SUBMIT",command=give3,bg='yellow')
        new3_submit.grid(row=3,column=0)
        new3_back=Button(new3,text="BACK",command=new3.destroy,bg='yellow')
        new3_back.grid(row=3,column=1)
        

    def UPDATE():
        cnx=mysql.connector.connect(user='root',password="tiger",host="localhost",database="SCAMAZON")
        cur=cnx.cursor()
        top5=Toplevel()
        top5.geometry("450x250")
        top5.configure(bg='orange')
        top5.title("UPDATE")
        top5.iconbitmap(r'd:\python\scam.ico')
        update1_=Button(top5,text="CHANGE NAME",command=update1,padx=40,pady=20,bg="skyblue",foreground="red")
        update1_.grid(row=0,column=0)

        update2_=Button(top5,text="CHANGE PHONE NUMBER",command=update2,padx=40,pady=20,bg="skyblue",foreground="red")
        update2_.grid(row=0,column=1)

        update3_=Button(top5,text="CHANGE ADRESS",padx=40,command=update3,pady=20,bg="skyblue",foreground="red")
        update3_.grid(row=1,column=0)

        update4_=Button(top5,text="CHANGE MULTIPLE",padx=40,command=update4,pady=20,bg="skyblue",foreground="red")
        update4_.grid(row=1,column=1)

        BackButton=Button(top5,text="BACK",command=top5.destroy,padx=40,pady=20,bg="skyblue",foreground="red")
        BackButton.grid(row=2,column=0)
    cnx=mysql.connector.connect(user='root',password="tiger",host="localhost",database="SCAMAZON")
    cur=cnx.cursor()
    
def InsertMember():
    top=Toplevel()#page2
    top.geometry("400x300")
    top.title("NEW ENTRY")
    top.configure(bg='pink2')
    top.iconbitmap(r'd:/python/scam.ico')
    #Mname=input("enter your name")
     
    #create submit function
    def submit():

        import mysql.connector
        cnx=mysql.connector.connect(user='root',password="tiger",host="localhost",database="SCAMAZON")
        cur=cnx.cursor()
        try:
            q="select*from MEMBER"
            cur.execute(q)
            p=cur.fetchall()
            Mno="M000"+str(cur.rowcount+1)
            current_Date = datetime.datetime.now()
            formatted_date = current_Date.strftime('%Y-%m-%d %H:%M:%S') 
            if PASSWORD2_.get()==PASSWORD1_.get():
                s1="insert into Member values('{}','{}',{},'{}','{}')".format(Mno,Mname_.get(),int(MOB_.get()),current_Date,ADR_.get())
                s2="insert into Password values('{}',{})".format(Mno,int(PASSWORD1_.get()))
            
                cur.execute(s1)
                cur.execute(s2)
                print("RECORD INSERTED")
                print("YOUR MEMBERSHIP NUMBER(Mno) is",Mno) 
            else:
                print("PASSWORD MISSMATCH")
           
            #clear text boxes
            Mname_.delete(0,END)
            MOB_.delete(0,END)
            ADR_.delete(0,END)
            
            cnx.commit()
            cnx.close()
                     
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("SOMETHING IS WRONG WITH YOUR USER NAME OR PASSWORD")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("DATABASE DOES NOT EXIST")
            else:
                print(err)
        else:
            cnx.close()

    #creating text boxes
    Mname_=Entry(top,width=30,bg='skyblue')
    Mname_.grid(row=0,column=1,padx=20)

    MOB_=Entry(top,width=30,bg='skyblue')
    MOB_.grid(row=1,column=1)

    ADR_=Entry(top,width=30,bg='skyblue')
    ADR_.grid(row=2,column=1)

    PASSWORD1_=Entry(top,width=30,bg='skyblue',show='*')
    PASSWORD1_.grid(row=3,column=1)
   
    PASSWORD2_=Entry(top,width=30,bg='skyblue',show='*')
    PASSWORD2_.grid(row=4,column=1)
      
   #CREATING TEXT BOXES LABLES
    Mname_label=Label(top,text="ENTER YOUR NAME",foreground='red',bg='pink2')
    Mname_label.grid(row=0,column=0)

    MOB_label=Label(top, text="MOBILE NUMBER",foreground='red',bg='pink2')
    MOB_label.grid(row=1,column=0)
    
    ADR_label=Label(top,text="ENTER ADDRESS",foreground='red',bg='pink2')
    ADR_label.grid(row=2,column=0)

    PASSWORD1_label=Label(top,text="ENTER YOUR PASSWORD",foreground='red',bg='pink2')
    PASSWORD1_label.grid(row=3,column=0)

    PASSWORD2_label=Label(top,text="ENTER YOUR PASSWORD AGAIN",foreground='red',bg='pink2')
    PASSWORD2_label.grid(row=4,column=0)
    
    #CREATE A SUBMIT BUTTON
    
    submit_btn=Button(top,text="ADD RECORDS",command=submit,bg="purple",foreground="yellow")
    submit_btn.grid(row=5,column=0,columnspan=4,pady=15,padx=10,ipadx=100)

    #entering EXITING
    submit_btn2=Button(top,text="BACK",command=top.destroy,bg="purple",foreground="yellow")
    submit_btn2.grid(row=7,column=0,columnspan=4,pady=15,padx=10,ipadx=100)

    #CREATE QUERY BUTTON
    query_btn=Button(top,text="PROCEED",command=Login,bg="purple",foreground="yellow")
    query_btn.grid(row=6,column=0,columnspan=4,pady=15,padx=10,ipadx=100)
def entry():
    TOP=Toplevel()
    TOP.configure(bg="yellow")
    TOP.iconbitmap(r'd:\python\scam.ico')
    button_1=Button(TOP,text="CREATE AN ACCOUNT",padx=40,pady=20,foreground='black',command=InsertMember,bg='yellow')
    button_2=Button(TOP,text="SIGN IN",foreground='red',padx=40,pady=20,command=Login,bg='skyblue')
    button_3=Button(TOP,text="QUIT",foreground='white',padx=40,pady=20,command=root.destroy,bg='purple')

    #my_label = Label(root,image=my_img)
    #my_label.pack()#(row=0,column=0,columnspan=3)
# put button on screen

    #definig buttons
    button_1.grid(row=1,column=0)
    button_2.grid(row=1,column=1)
    button_3.grid(row=1,column=2) 
    
def multi():
    root.forget
    entry()

def query():
    global root
    #inserting image
    my_img=PhotoImage(file="d:\\python\\scamazon.png")


    button_1=Button(root,text="WELCOME TO SCAMAZON",padx=40,pady=20,foreground='black',command=multi,bg='yellow')
    #button_2=Button(root,text="SIGN IN",foreground='red',padx=40,pady=20,command=Login,bg='skyblue')
    #button_3=Button(root,text="QUIT",foreground='white',padx=40,pady=20,command=root.destroy,bg='purple')

    my_label = Label(root,image=my_img)
    my_label.pack()#(row=0,column=0,columnspan=3)
# put button on screen

    #definig buttons
    button_1.pack()#(row=1,column=)
    button_2.grid()#(row=1,column=1)
    #button_3.grid(row=1,column=2)    
query()
#sell()


























