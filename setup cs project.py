import mysql.connector
cnx=mysql.connector.connect(user="root",password="tiger",host="localhost")
cur=cnx.cursor()
s1="CREATE DATABASE SCAMAZON"
cur.execute(s1)

s="use SCAMAZON"
cur.execute(s)

s2="create table Cart(Ino VARCHAR(10),Mno VARCHAR(10),Price int,QTY INT)"
cur.execute(s2)

s3="create table Itemrecord(Ino VARCHAR(10) PRIMARY KEY,Iname VARCHAR(50),Manu VARCHAR(50),Price int,QTY INT,DOP DATE)"
cur.execute(s3)

s4="create table Member(Mno VARCHAR(10) PRIMARY KEY,Mname varchar(30),MOB INT(20),DOM DATE,ADR VARCHAR(50))"
cur.execute(s4)

s5="create table PASSWORD(Mno VARCHAR(10) PRIMARY KEY,PASSWORD INT(10))"
cur.execute(s5)

cnx.commit()
