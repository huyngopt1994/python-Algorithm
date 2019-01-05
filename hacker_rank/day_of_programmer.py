# https://www.hackerrank.com/challenges/day-of-the-programmer/problem
mapping_month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap_julian(year):
    return (year % 4 == 0)


def is_leap_grego(year):
    return (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))


def calculate_date_with_normal_year(custom_year):
    # find the 256 th day in this year
    total_day = 256
    month = 0
    day = 0
    result = '{}.{}.{}'
    for index, month in enumerate(mapping_month_days):
        total_day -= month
        if total_day <= 0:
            total_day += mapping_month_days[index]
            month = index + 1
            day = total_day
            break
    if month < 10:
        month_to_str = '0{}'.format(month)
    else:
        month_to_str = str(month)
    if day < 10:
        day_to_str = '0{}'.format(day)
    else:
        day_to_str = str(day)

    return result.format(day_to_str, month_to_str, custom_year)


def find_programmer_day(custom_year):
    if custom_year < 1918:
        # julian year
        if is_leap_julian(custom_year):
            mapping_month_days[1] = 29

    elif custom_year > 1918:
        # grego year
        if is_leap_grego(custom_year):
            mapping_month_days[1] = 29
    else:
        mapping_month_days[1] = 15
    return calculate_date_with_normal_year(custom_year)


my_year = int(input())
result = find_programmer_day(my_year)
print(result)
