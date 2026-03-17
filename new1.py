import pymssql

server="mssqlericdb1.database.windows.net"
user="john"
password="abc-12345"
database="free-sql-db-7651785"

connect=pymssql.connect(server,user,password,database)
print ("登入成功")

cursor=connect.cursor()
print("cursor成功")

cursor.execute("select * from stocks")
print("查詢成功")

records=cursor.fetchall()

rec_count=len(records)

print(f'總共查詢到{rec_count}筆資料')