import pandas as pd
# 1stNameisAtul
chunksize = 10
for chunk in pd.read_csv('inputfile.txt', chunksize=chunksize):
    a = chunk[0:3]
    b = chunk[3:7]
    c = chunk[7:9]
    d = chunk[9:13]
    print("atul")

print("a,b,c,d is : ",a,b,c,d)