import mysql.connector

def add_profession():
    mydb = mysql.connector.connect(
        host="localhost",
        username="root",
        passwd="",
        database="salaray_manage_sys")
    cursor = mydb.cursor()
    print("___________ Add New Profession ___________")
    print("Go Back : Enter '000' ")
    professioncode = int(input("Enter Profession Code : "))
    if professioncode==000:
        print("OK!")    
    else:
        profession = input("Enter Profession : ")
        dailyrate = float(input("Enter Daily Rate : "))
        sql = "insert into profession values(%s, %s, %s)"
        val = (professioncode,profession,dailyrate)
        cursor.execute(sql,val)
        mydb.commit()
        print("Added✅")
        
    cursor.close()
    mydb.close()
    
add_profession()