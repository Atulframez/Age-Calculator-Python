import time
from calendar import isleap
from datetime import datetime

def get_zodiac_sign(day, month):
    if month == 12:
        return 'Sagittarius' if (day < 22) else 'Capricorn'
    elif month == 1:
        return 'Capricorn' if (day < 20) else 'Aquarius'
    elif month == 2:
        return 'Aquarius' if (day < 19) else 'Pisces'
    elif month == 3:
        return 'Pisces' if (day < 21) else 'Aries'
    elif month == 4:
        return 'Aries' if (day < 20) else 'Taurus'
    elif month == 5:
        return 'Taurus' if (day < 21) else 'Gemini'
    elif month == 6:
        return 'Gemini' if (day < 21) else 'Cancer'
    elif month == 7:
        return 'Cancer' if (day < 23) else 'Leo'
    elif month == 8:
        return 'Leo' if (day < 23) else 'Virgo'
    elif month == 9:
        return 'Virgo' if (day < 23) else 'Libra'
    elif month == 10:
        return 'Libra' if (day < 23) else 'Scorpio'
    elif month == 11:
        return 'Scorpio' if (day < 22) else 'Sagittarius'

def judge_leap_year(year):
    return isleap(year)

def month_days(month, leap_year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2 and leap_year:
        return 29
    elif month == 2 and (not leap_year):
        return 28


name = input("Please enter your name: ")
age = input("Please enter your age: ")
localtime = time.localtime(time.time())

year = int(age)
month = year * 12 + localtime.tm_mon
day = 0

begin_year = int(localtime.tm_year) - year
end_year = begin_year + year

for y in range(begin_year, end_year):
    if (judge_leap_year(y)):
        day = day + 366
    else:
        day = day + 365

leap_year = judge_leap_year(localtime.tm_year)
for m in range(1, localtime.tm_mon):
    day = day + month_days(m, leap_year)

day = day + localtime.tm_mday
print("\n\t%s's age is %d years or " % (name, year), end="")
print("%d months or %d days" % (month, day))

# --- NEW FEATURE: EXACT DOB & ZODIAC ---
print("\n" + "="*40)
dob_input = input("For exact details, enter your Date of Birth (YYYY-MM-DD) or press Enter to skip: ")
if dob_input.strip():
    try:
        dob = datetime.strptime(dob_input.strip(), "%Y-%m-%d")
        now = datetime.now()
        
        # Calculate Exact Days
        delta = now - dob
        
        # Day of the week
        day_of_week = dob.strftime("%A")
        
        # Zodiac Sign
        zodiac = get_zodiac_sign(dob.day, dob.month)
        
        print("\n\t--- Detailed Analysis ---")
        print(f"\tExact Days Lived : {delta.days:,} days")
        print(f"\tDay of the Week  : {day_of_week}")
        print(f"\tZodiac Sign      : {zodiac}")
        print("\t" + "="*25 + "\n")
        
    except ValueError:
        print("\n\tInvalid date format. Skipping detailed analysis.\n")

# Daily commit: 49