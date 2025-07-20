import mysql.connector

def load_empdata():
    mydb = mysql.connector.connect(
        host="localhost",
        username="root",
        passwd="",
        database="salaray_manage_sys")
    cursor = mydb.cursor()
    print("___________ Load Employee Data ___________")
    txtlocate=input("Enter Data File Name with Location : ")
    
    file = open(txtlocate,"r")
    line = file.readline()
    print("🔄 Please wait, loading...")
    while not(line == ""):
        txtdata=line.split("\t")
        #print(txtdata)
        whnum=1
        while not(whnum==13):
            if whnum == 1:
                sql="insert into employee values(%s, %s, %s)"
                val=(txtdata[0],txtdata[1],int(txtdata[2]))
                cursor.execute(sql,val)
                mydb.commit()
            sql="insert into workeddata values(%s,%s,%s)"
            val=(txtdata[0],whnum,int(txtdata[whnum+2]))
            cursor.execute(sql,val)
            whnum +=1
            mydb.commit()
        line = file.readline()
    print("All Data Added✅")
    cursor.close()
    mydb.close()
    
load_empdata()