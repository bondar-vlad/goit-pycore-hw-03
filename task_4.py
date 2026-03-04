from datetime import datetime, timedelta

# Параметр функції users — це список словників, де кожен словник містить ключі name (ім'я користувача, рядок) та birthday (день народження, рядок у форматі 'рік.місяць.дата').
# Функція має визначати, чиї дні народження випадають вперед на 7 днів включаючи поточний день. Якщо день народження припадає на вихідний, дата привітання переноситься на наступний понеділок.
# Функція повертає список словників, де кожен словник містить інформацію про користувача (ключ name) та дату привітання (ключ congratulation_date, дані якого у форматі рядка 'рік.місяць.дата').
def get_upcoming_birthdays(users: list[dict]):
    upcoming_birthdays = []
    today = datetime.today().date()

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = datetime(year=today.year, month=birthday.month, day=birthday.day).date()
        if birthday_this_year < today:
            birthday_this_year = datetime(year = today.year + 1, month = birthday.month, day = birthday.day).date()
        days_difference = (birthday_this_year - datetime.today().date()).days
        if (days_difference >= 0 and days_difference < 7):
            birthday_weekday = birthday_this_year.isoweekday()
            congratulation_date = birthday_this_year if birthday_weekday < 6 else birthday_this_year + timedelta(days=8-birthday_weekday)
            upcoming_birthdays.append({"name":user["name"], "congratulation_date":congratulation_date})
    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.03.05"},
    {"name": "Jane Smith", "birthday": "1990.03.07"},
    {"name": "Jane Smith", "birthday": "1990.03.04"},
    {"name": "Jane Smith", "birthday": "1990.02.11"}
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
