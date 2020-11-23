from datetime import date
from datetime import time
from datetime import datetime
import calendar

def main():
    # today = date.today()
    # print("Today's date is ", today)

    # print("Date components: ", today.day, today.month, today.year)

    # print ("Today's weekday # is: ", today.weekday())

    # days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]

    # print ("Which is a: ", days[today.weekday()])
    c = calendar.TextCalendar(calendar.SUNDAY)


    today = datetime.now()
    print ("The current date time is ", today)

    t = datetime

    for i in c.itermonthdays(2017, 8):
        print(i)

    for name in calendar.month_name:
        print(name)

    for m in range(1, 13):
        cal = calendar.monthcalendar(2018, m)
        weekone = cal[0]
        weektwo = cal[1]

        if weekone[calendar.FRIDAY] != 0:
            meetday = weekone[calendar.FRIDAY]
        else:
            meetday = weektwo[calendar.FRIDAY]

        print("%10s %2d" % (calendar.month_name[m], meetday))


if  __name__ == '__main__':
    main()