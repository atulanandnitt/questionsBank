import os
 
# The top argument for walk
parentdir = '.'
# The extension to search for
exten = '.py'
extens=['.py','.txt','.csv']


# What will be logged

print(os.walk(parentdir))
def method1():
    results = str()
    logname = 'findfiletype1.log'
    for dirpath, subdirList, fileList in os.walk(parentdir):
        for fname in fileList:
            for item in extens:
                if fname.lower().endswith(item):
                    # Save to results string instead of printing
                    results += '%s\n' % os.path.join(dirpath, fname)
 
    # Write results to logfile
    with open(logname, 'w') as logfile:
        logfile.write(results)            

def method2():
    results = str()
    logname = 'findfiletype2.log'
    for dirpath, subdirList, fileList in os.walk(parentdir):
        for fname in fileList:
            extnofFile="."+fname.split(".")[-1]
            print("extnofFile",extnofFile)
            if extnofFile in extens:
                    # Save to results string instead of printing
                    results += '%s\n' % os.path.join(dirpath, fname)
     
    # Write results to logfile
    with open(logname, 'w') as logfile:
        logfile.write(results)            
        
method1()
method2()    
#os.remove("findfiletype2.log")    