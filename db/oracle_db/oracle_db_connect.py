import cx_Oracle
print("try to connect")
con = cx_Oracle.connect('GCP_BQ_POC/Admin123@52.229.14.226:1521/orcldb')
print (con.version)
con.close()