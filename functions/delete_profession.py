import mysql.connector

def delete_profession():
    mydb = mysql.connector.connect(
        host="localhost",
        username="root",
        passwd="",
        database="salaray_manage_sys")
    cursor = mydb.cursor()
    print("___________ Delete Profession ___________")
    professioncode = input("Enter Profession Code You Want to Delete : ")
    yesno = input("Are you Sure?/, you Want To Remove %s (Y/N) : "%professioncode)
    if yesno == "Y" or yesno == "y":
        sql = "delete from profession where ProfessionCode=%s"
        val = (professioncode,)
        cursor.execute(sql,val)
        mydb.commit()
        print("%s Deleted✅"%professioncode)  
    else:print("Ok!")
    cursor.close()
    mydb.close()
 
delete_profession()