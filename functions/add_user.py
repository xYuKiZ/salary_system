import getpass
import mysql.connector

def add_user():
    mydb = mysql.connector.connect(
        host="localhost",
        username="root",
        passwd="",
        database="salaray_manage_sys")
    cursor = mydb.cursor()
    print("___________ Add New App User ___________")
    username = input("Enter User Name : ")
    password = getpass.getpass("Enter User Password : ")
    confirm_password = getpass.getpass("Confirm Password : ")
    if password == confirm_password:
        user_type = input("Enter User Type (owner/admin) : ")
        sql = "insert into appuser (Username,Password,UserType) values(%s, %s, %s)"
        val = (username,password,user_type)
        cursor.execute(sql,val)
        mydb.commit()
        print("Added✅")    
    else:
        print("Password Not Match❌")
    cursor.close()
    mydb.close()

add_user()