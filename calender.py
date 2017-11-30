import calendar

try:
    year = int(input("Enter the year for you want to see the calendar: "))
    if year <1 or year > 9999:
        print("Select Proper year between 1 and 9999")
    else:
        for i in range(12):
            print(calendar.month(year,i+1))
except:
    print("Select the proper year")
            
