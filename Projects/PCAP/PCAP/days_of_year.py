def is_year_leap(year):
    r=False
    if year % 4 == 0 and not(year % 100 == 0 and year % 400 != 0):
        r=True
    return r

def days_in_month(year, month):
    if year < 1 or not(1 <= month <= 12):
        return
    return [31, [28, 29][is_year_leap(year)], 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month-1]

def day_of_year(year, month, day):
    return sum(map(days_in_month, [year for _ in range(month-1)], range(1, month))) + day

print(day_of_year(2000, 12, 31))
