#1#
import datetime
import os
import time

x = datetime.datetime.now()

print(x)

#2#
p = datetime.datetime(1,1,1)
print(p)

q = datetime.datetime.now()

print("år",q.year)
print("månad",q.month)
print("dag", q.day)


#3#
for n in range(0,10):
    a = datetime.datetime.now()
    time.sleep(1)
    print(a.strftime("%X"))

#4#
z = 0
for h in range(0,10):
    time.sleep(1)
    z = z +1 
    print(z)
    

#5#
#finns inget program som det hade passat i



#6#
year = input("skriv ett år:")
mon = input("skriv månad:")
day = input("skriv dag:")
now = datetime.datetime.now()
q = 0

if  mon == "2":
    q = 31
elif mon == "3":
    q = 59
elif mon == "4":
    q = 90
elif mon == "5":
    q = 120
elif mon == "6":
    q = 151
elif mon == "7":
    q = 181
elif mon == "8":
    q = 212
elif mon == "9":
    q = 243
elif mon == "10":
    q = 273
elif mon == "11":
    q = 304
elif mon == "12":
    q = 334

print("Det är en skilnad av\n",int(now.strftime("%Y")) - int(year),"år\n",int(now.strftime("%m")) - int(mon),"månader\n", int(now.strftime("%j")) - (q + int(day)) ,"dagar")


#7#
klock = input("hur läng timer vill du ha:")
for u in range(0,int(klock)):
    print(klock)
    klock = int(klock) - 1
    time.sleep(1)
    if int(klock) == 0:
        print("tidne är slut")