
a = "1"
a=int(a)
b = 2
print(a + b)



a = "1"
b = 2
b=str(b)
print(a + b)


c="My name 'is  Atul"
print(c)

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[3])

print(letters[:3])

print(letters[-2: ])

for item in letters:
    print(item)
    
print(range(0,len(letters),1))
print(range(len(letters)))
    
for i in range(0,len(letters),2):
    print(letters[i])    