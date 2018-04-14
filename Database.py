import sqlite3

def create_table():
    conn = sqlite3.connect("LicenceRecognize.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS admin (Name TEXT,Pass TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS cars (NationalId INTEGER,OwnerName TEXT,Model TEXT,Address TEXT,PhoneNumber INTEGER,color TEXT,LicensePlate TEXT,TotalFines INTEGER)")

    conn.commit()
    conn.close()

def insert1(Name,Pass):
    conn=sqlite3.connect("LicenceRecognize.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO admin (Name,Pass) VALUES (?,?)",(Name,Pass))
    conn.commit()
    conn.close()

def insert2(NationalId,OwnerName,Model,Address,PhoneNumber,color,LicensePlate,TotalFines):
    conn=sqlite3.connect("LicenceRecognize.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO cars (NationalId,OwnerName,Model,Address,PhoneNumber,color,LicensePlate,TotalFines) VALUES (?,?,?,?,?,?,?,?)",(NationalId,OwnerName,Model,Address,PhoneNumber,color,LicensePlate,TotalFines))
    conn.commit()
    conn.close()

def view1():
    conn = sqlite3.connect("LicenceRecognize.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM admin")
    rows = cur.fetchall()
    conn.close()
    return rows

def view2():
    conn = sqlite3.connect("LicenceRecognize.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM cars")
    rows = cur.fetchall()
    conn.close()
    return rows

def check1(Name,Pass):
    conn = sqlite3.connect("LicenceRecognize.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM admin WHERE Name=? AND Pass=?",(Name,Pass))
    rows = cur.fetchall()
    conn.close()
    if len(rows) > 0:
        return True
    return False
def check2(license):
    conn = sqlite3.connect("LicenceRecognize.db")
    cur = conn.cursor()
    print license
    cur.execute("SELECT * FROM cars WHERE LicensePlate=?",(license,))
    rows = cur.fetchall()
    conn.close()
    return rows


create_table()
# insert1("Ahmed","1414")
# insert2(190078,"Elon","Tesla","California",0124575325,"red","L0LWATT",150)
# print "First View:"
# print view1()
# print "Second Table"
print view2()
# print check2("LOLWATT")
# print check1('Ahmed','ass')
