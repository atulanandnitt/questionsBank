import os
 
# The top argument for walk
parentdir = '.'
# The extension to search for
exten = '.py'
logname = 'findfiletype.log'
# What will be logged
results = str()

print(os.walk(parentdir))
 
for dirpath, subdirList, fileList in os.walk(parentdir):
    for fname in fileList:
        if fname.lower().endswith(exten):
            # Save to results string instead of printing
            results += '%s\n' % os.path.join(dirpath, fname)
 
# Write results to logfile
with open(logname, 'w') as logfile:
    logfile.write(results)            
    