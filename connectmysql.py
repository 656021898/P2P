import pymysql

connectInfo = pymysql.Connect(
    host="47.107.168.87",
    port= 3306,
    user="python",
    password="python666",
    db="test"
)

cur = connectInfo.cursor()
print(cur.execute("show TABLES"))