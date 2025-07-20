import mysql.connector

def get_profession(professioncode):
    mydb = mysql.connector.connect(
        host="localhost",
        username="root",
        passwd="",
        database="salaray_manage_sys")
    cursor = mydb.cursor()
    sql = "select * from profession where ProfessionCode=%s"
    val = (professioncode,)
    cursor.execute(sql,val)
    result = cursor.fetchall()
    cursor.close()
    mydb.close()
    return result

def edit_profession():
    mydb = mysql.connector.connect(
        host="localhost",
        username="root",
        passwd="",
        database="salaray_manage_sys")
    cursor = mydb.cursor()
    print("___________ Change Profession Details ___________")
    professioncode = int(input("Enter Profession Code : "))
    print("_________________________________")
    
    professionresult=get_profession(professioncode)
    
    print("Profession Code : %d"%professionresult[0][0])
    print("Profession : %s"%professionresult[0][1])
    print("Daily Rate : %s"%professionresult[0][2])
    print("_________________________________")
    print("Profession Name(N)")
    print("Daily Rate(R)")
    print("Both(B)")
    
    choice = input("Enter Choice : ")
    
    if choice== "N" or choice=="n":
        professionname=input("Enter New Profession Name : ")
        sql = "update profession set ProfessionName=%s where ProfessionCode=%s"
        val = (professionname,professioncode)
        cursor.execute(sql,val)
        mydb.commit()
        print("%d Profession Name Updated✅"%professioncode)
        
    if choice== "R" or choice=="r":
        dailyrate=float(input("Enter New Daily Rate : "))
        sql = "update profession set DailyRate=%s where ProfessionCode=%s"
        val = (dailyrate,professioncode)
        cursor.execute(sql,val)
        mydb.commit()
        print("%d Daily Rate Updated✅"%professioncode)
        
    if choice== "B" or choice=="b":
        professionname=input("Enter New Profession Name : ")
        dailyrate=float(input("Enter New Daily Rate : "))
        sql = "update profession set ProfessionName=%s,DailyRate=%s where ProfessionCode=%s  "
        val = (professionname,dailyrate,professioncode)
        cursor.execute(sql,val)
        mydb.commit()
        print("%d Profession Name & Daily Rate Updated✅"%professioncode)
        
    cursor.close()
    mydb.close()
    
edit_profession()

