import mysql.connector


def firstProgramme():
    mycon = mysql.connector.connect(host="localhost", user='root', passwd='root', database='demo')
    print(mycon)
    cursor = mycon.cursor()
    print(cursor)
    sql = "insert into student(id,name) values(%s,%s)"
    val = (7, "Santi RAm")
    try:
        # cursor.(sql,val)
        cursor.execute("select * from student")
        result = cursor.fetchall()
        mycon.commit()
        # getting the lst row id las
        print(cursor.lastrowid)
    except:
        print("This block is executed ")
        mycon.rollback()
    print("printing the rowcount of the cursor las ")
    print(cursor.rowcount)
    pass

def Getting_Data_From_DataBase():
    con=mysql.connector.connect(host='localhost',user='root',passwd='root',database ='demo')
    sql='select * from student'
    cursor=con.cursor()

    try:
        cursor.execute(sql)
        result=cursor.fetchall()
    except:
        con.rollback()

    print("Printng the all the values present in the cursor las ")
    for s  in result:
        print(s)
    pass

def main():
    Getting_Data_From_DataBase()
    pass

if __name__ == '__main__':
    main()
