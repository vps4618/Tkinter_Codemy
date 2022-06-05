import datetime;
import calendar
today = str(datetime.date.today())
curr_year = int(today[:4])
curr_month = int(today[5:7])

month_number = list(calendar.month_abbr)
month_number=month_number[curr_month]
print(month_number)
