f = open("notepad.txt", 'r')
#print(f.read())
#print(f.readline())

f1 = open("abc.txt", 'w')
f1.write("something")
f1.write("Incredible")

f1 = open("abc.txt",'a')
f1.write(" /n  Incredible India")

#for data in f:
 #   print(data)

for data in f:
    f1.write(data)

f2 = open("IMG_3209.JPG", 'rb')
f3 = open("Mypic.JPG", 'wb')
for i in f2:
    f3.write(i)


