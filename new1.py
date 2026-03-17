import pymssql

server="mssqlericdb1.database.windows.net"
user="john"
password="!Rhea95032"
database="free-sql-db-7651785"

connect=pymssql.connect(server,user,password,database)

print ("登入成功")