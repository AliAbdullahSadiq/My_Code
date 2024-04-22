from datetime import datetime

Date_Right_Now = datetime.now()
Date_of_Birth = datetime(2005, 4, 19) # (year, month, day, hour, minute, second, microsecond)

DateInput = input('Input Date (eg: yyyy-mm-dd): ') # will be string
year, month, day = map(int, DateInput.split('-')) # maps string to datetime
UserDate = datetime(year, month, day)

MMDDYYYY = UserDate.strftime("%m/%d/%Y") #changing format to month day year
DDMMYYYY = UserDate.strftime("%d/%m/%Y") #changing format to day month year

print(Date_Right_Now)
print(Date_of_Birth)
print(DateInput)
print(UserDate)
print(MMDDYYYY)
print(DDMMYYYY)