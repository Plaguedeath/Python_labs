
from datetime import datetime

def get_zodiac_by_date(birth_date):
    
    month = birth_date.month
    day = birth_date.day
    
    zodiac_dates = [
        (1, 20, "Capricorn"), (2, 19, "Aquarius"), (3, 21, "Pisces"),
        (4, 20, "Aries"), (5, 21, "Taurus"), (6, 21, "Gemini"),
        (7, 23, "Cancer"), (8, 23, "Leo"), (9, 23, "Virgo"),
        (10, 23, "Libra"), (11, 22, "Scorpio"), (12, 22, "Sagittarius")
    ]
    
    for end_month, end_day, sign in zodiac_dates:
        if (month < end_month) or (month == end_month and day <= end_day):
            return sign
    
    return "Capricorn"  



date_str = input("Введите дату рождения (в формате: 27.10):")

data_object = datetime.strptime(date_str,"%d.%m")

sign = get_zodiac_by_date(data_object)
print(f"Birth date: {date_str} -> Zodiac sign: {sign}")