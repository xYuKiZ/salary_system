import mysql.connector

def delete_user():
    mydb = mysql.connector.connect(
        host="localhost",
        username="root",
        passwd="",
        database="salaray_manage_sys")
    cursor = mydb.cursor()
    print("___________ Remove App User ___________")
    username = input("Enter User Name : ")
    yesno = input("Are you Sure?/, you Want To Remove %s (Y/N) : "%username)
    if yesno == "Y" or yesno == "y":
        sql = "delete from appuser where username=%s"
        val = (username,)
        cursor.execute(sql,val)
        mydb.commit()
        print("%s Deleted✅"%username)  
    else:print("Ok!")
    cursor.close()
    mydb.close()

delete_user()