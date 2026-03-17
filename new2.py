import pymssql
import random
import time

server="mssqlericdb1.database.windows.net"
user="john"
password="abc-12345"
database="free-sql-db-7651785"

INS_SQL="""
    INSERT INTO dbo.stocks(sid,sname,sprice)
    VALUES(
        %s,
        %s,
        %d
    )
"""
try:
    connect=pymssql.connect(server,user,password,database)
    cursor=connect.cursor()
    for i in range(1,30):
        rp=random.randint(1800,1999)
        cursor.execute(INS_SQL,("2330","TSMC",rp))
        connect.commit
    print(f'第{i}次擷取,金額 {rp}')
    if( i < 30 ):  
        time.sleep(3)
        
    connect.close()
    cursor.close()
except Exception as e: 
    print(f'連線失敗: 原因{e}')