def euler19():
    f = open('log.txt', 'w')
    calendar = 0
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    count = int(raw_input('What day, 0-6, was Jan 1st, 1900? '))
    for year in range(1900,2001):
        if (year%4 == 0):
            if (year%100 == 0) and (year%400 != 0):
                months[1] = 28
            else:
                months[1] = 29
        else:
            months[1]=28
        for month in range(0,12):
            for day in range(1,months[month]+1):
                count = count%7
                if year > 1900 and day == 1 and count == 0:
                    calendar += 1
                    f.write('%d/%d/%d\n' %(month+1, day, year))
                count += 1
    f.close()
    return calendar

        
def etest():
    f = open('tlog.txt', 'w')
    calendar = 0
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    count = int(raw_input('What day, 0-6, was Jan 1st, 1900? '))
    for year in range(1900,1910):
        if (year%4 == 0):
            if (year%100 == 0) and (year%400 != 0):
                months[1] = 28
            else:
                months[1] = 29
        else:
            months[1]=28
        for month in range(0,12):
            for day in range(1,months[month]+1):
                count = count%7
                if day == 1:
                    f.write('%d/%d/%d: %d\n' %(month+1, day, year, count))
                count += 1
    f.close()
    return calendar