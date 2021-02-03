#Connor Fryhofer 1853826
print('Birthday Calculator')
print('Current day')
m = int(input('Month: '))
d = int(input('Year: '))
y = int(input('Year: '))
print('Birthday')
m2 = int(input('Month: '))
d2 = int(input('Day: '))
y2 = int(input('Year: '))
amtyears = y-y2-1
if(m2<m):
    amtyears+=1
elif(m==m2):
    if(d2<d):
        amtyears+=1
if(m==m2 and d==d2):
    print('Happy Birthday')
print('You are '+str(amtyears)+" years old.")
