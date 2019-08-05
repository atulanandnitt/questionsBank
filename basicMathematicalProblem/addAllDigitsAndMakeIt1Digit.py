def addAllDigitsAndMakeIt1Digit(str1):
    val=0
    if len(str(str1)) == 1 and int(str1) < 9:
        return int(str1)
    else:
        val= int (int(str1[0]) + int(str1[1]))
        if val <10:
            addAllDigitsAndMakeIt1Digit(str(str(val) + str1[2:]))
        else:
            val = val /10 + val%10
            addAllDigitsAndMakeIt1Digit(str(str(val) + str1[2:]))

str1=str(1234)
#print(int(str1[0]) + int(str1[1]))
print(addAllDigitsAndMakeIt1Digit(str1))    