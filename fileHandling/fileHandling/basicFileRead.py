
def sum1(a,b):
    return a+b



def sum1(a,b):
    return a+b


sol=sum1(30,40)
f = open('output.txt', 'w')
resultstr = str(sol)
f.write(str(sum1(31,41)))
f.close()





def FindDetailsOfParticularFile(absfileName):
    result = []

    print(absfileName)
    with open(absfileName, 'r') as f:
        for line in f:
            result.append(line)
            print(line)



    f = open('input.txt', 'r')
    print(f.read())
    f.close()




absfileName = "REL8_QM_ActualSeasonality_1.dif"
# FindDetailsOfParticularFile('D:\CRM\Sprint\R13_18-05_sprint6_Partner Program\REST_API\python\objective_doubts\basicDataStructure\fileHandling\REL8_QM_ActualSeasonality_1.dif')
FindDetailsOfParticularFile(absfileName)



n = int(input())
print(n, type(n))


