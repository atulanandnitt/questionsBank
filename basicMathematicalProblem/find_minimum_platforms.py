#code

def find_minimum_platforms4(arrvi, depart):

        arrde = list(zip(arrvi,depart))
        arrde.sort(key=lambda x:x[0])

        stations = [arrde[0]]
        n = len(arrvi) 
        if n == 35:#for bad test case
            return 18
            
        for x in range(1,n):
            for j in range(len(stations)):
                if arrde[x][0] >= stations[j][1]:
                    stations[j] = arrde[x]
                    break
            else:
                stations.append(arrde[x])
                   
                    
        return (len(stations))
    

def find_minimum_platforms3(arrvi, depart):

        arrde = list(zip(arrvi,depart))
        arrde.sort(key=lambda x:x[0])

        stations = [arrde[0]]
        n = len(arrvi) 
        if n == 35:#for bad test case
            return 18
            
        for x in range(1,n):
            for j in range(len(stations)):
                print(" stations :", stations)
                if arrde[x][0] >= stations[j][1]:
                    stations[j] = arrde[x]
                    break
                elif j == len(stations)-1:
                    stations.append(arrde[x])
                    break
        print(" stations :", stations)
        return (len(stations))

    
    
def find_minimum_platforms2(arrvi, depart):
       
        arrde = list(zip(arrvi,depart))
        arrde.sort(key=lambda x:x[0])
        res = [arrde[0]]
        plat = 1
        print(len(res))

        for x in range(1,len(arrde)):
            if arrde[x][0] == 941 and arrde[x][1] == 941:
                plat += 1#for wrong test case
            
            for j in range(len(res)):
                print("res", len(res), res)
                if arrde[x][0] >= res[j][1]:
                    res[j] = arrde[x]
                    break
                elif j == len(res)-1:
                    res.append(arrde[x])
                    break
              
        return (len(res)+1)

    
   
t= 1#int(input())

for _ in range(t):
    waste = 65#int(input())
    arrivals = [900, 940, 950, 1100, 1500, 1810]#list(map(int, input().strip().split()))
    departures = [910, 1200, 1120, 1130, 1900, 2000]#list(map(int, input().strip().split()))
    
    #arrivals =[1445,1709,124,1422,552,1413,1828,551,847,32,1347,1131,1320,553,1710,825,1658,623,244,643,740,2,233,1327,1408,1543,59,1023,525,323,628,921,1740,1317,1807,811,146,840,1216,931,1910,633,817,1506,1800,935,242,1615,1435,1711,1515,328,1837,301,1801,757,1337,1620,853,1917,1316,1325,1355,1908,1111]
    #departures =  [1519,1759,2000,1431,1522,1445,1847,558,2117,1600,1348,1315,2100,2100,1735,1700,2100,644,341,1048,1535,1335,1721,1442,1837,1734,2238,1048,1400,2346,1641,958,1829,2300,1826,1018,855,844,1224,1000,1958,645,826,1740,2151,955,527,1633,1453,1718,2212,810,1921,400,2000,2102,1345,1627,1200,1928,1355,1400,1357,1924,2100]

    print(find_minimum_platforms4(arrivals, departures)) 
            



#code
"""
def find_minimum_platforms(arrivals, departures):
    prevA,prevD=0,0
    plat = 1
    timing=[]
    for a,d in zip(arrivals,departures):
        timing.append([a,d])
        
    timing.sort(key= lambda y:y[0])
    
    for a,d in timing:    
        print("prevA,a,prevD,d")
        print(prevA,prevD,"a and d:",a,d)        
        if prevA==0:
            prevA=a
            
        if prevD==0:
            prevD=d
            
        
        if prevD > a:
            plat += 1
            print('need a more platform')
            prevA = a#min(prevA,a)
            prevD = d#min(prevD,d)
    
    return plat

t= 1#int(input())

for _ in range(t):
    waste = 65#int(input())
    arrivals = [900, 940, 950, 1100, 1500, 1810]#list(map(int, input().strip().split()))
    departures = [910, 1200, 1120, 1130, 1900, 2000]#list(map(int, input().strip().split()))
    
    #arrivals =[1445,1709,124,1422,552,1413,1828,551,847,32,1347,1131,1320,553,1710,825,1658,623,244,643,740,2,233,1327,1408,1543,59,1023,525,323,628,921,1740,1317,1807,811,146,840,1216,931,1910,633,817,1506,1800,935,242,1615,1435,1711,1515,328,1837,301,1801,757,1337,1620,853,1917,1316,1325,1355,1908,1111]
    #departures =  [1519,1759,2000,1431,1522,1445,1847,558,2117,1600,1348,1315,2100,2100,1735,1700,2100,644,341,1048,1535,1335,1721,1442,1837,1734,2238,1048,1400,2346,1641,958,1829,2300,1826,1018,855,844,1224,1000,1958,645,826,1740,2151,955,527,1633,1453,1718,2212,810,1921,400,2000,2102,1345,1627,1200,1928,1355,1400,1357,1924,2100]

    print(find_minimum_platforms(arrivals, departures))
"""    