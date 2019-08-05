import cx_Oracle
print("try to connect")
con = cx_Oracle.connect('user_name/password@IP:port/sid')
print (con.version)
con.close()
