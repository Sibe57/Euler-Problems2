counter=0
last_day=1
def mounth_filler(number_of_mounth,number_of_year):
    day_of_mounth=[]
    if number_of_mounth==(4 or 6 or 8 or 10):
        for i in range(1,31):
            day_of_mounth.append(i)
    elif number_of_mounth==2:
        if number_of_year%400==0 or (number_of_year%4==0 and number_of_year%100!=0):
            for i in range(1,30):
                day_of_mounth.append(i)
        else:
            for i in range(1,29):
                day_of_mounth.append(i)
    else:
        for i in range(1,32):
            day_of_mounth.append(i)
    return day_of_mounth
def year(number=1900,first_day=1):
    mounths=[1,2,3,4,5,6,7,8,9,10,11,12]
    def next_day(today):
        return (today+1)%7
    a=first_day
    for i in mounths:
        mounth=mounth_filler(i,number)
        for g in mounth:
            if a==0 and g==1 and number!=1900:
                global counter
                counter+=1
                a = next_day(a)
            else:
                a=next_day(a)
    global last_day
    last_day=a
for t in range(1900,2001):
    year(t,last_day)
print(counter)








