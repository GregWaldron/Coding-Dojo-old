for x in range (1, 151):
    print (x)

for x in range (5, 1001, 5):
    print (x)

for x in range (1, 101):
    if x%10 == 0:
        print ("Coding Dojo")
    elif x%5 == 0:
        print ("Coding")
    else:
        print (x)

y=0

for x in range (0, 500001):
    y=x+y
    if x<500000:
        continue
    else:
        print (y)
        break

for x in range (2018, 0, -4):
    print (x)

lowNum=2
highNum=9
mult=3

for x in range (lowNum, highNum+1):
    if x%mult==0:
        print (x)