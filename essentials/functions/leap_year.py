def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False

    # if year % 4 != 0:
    #     return False
    # elif year % 100 != 0:
    #     return True
    # elif year % 400 != 0:
    #     return False
    # else:
    #     return True

def days_in_month(year, month):
    # if statement

    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # number id days month 1-12
    res = days[month-1]
    if month == 2 and is_year_leap(year):
        res = 29
    return res


def day_of_year(year, month, day):
    None

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
