import datetime

# Функція приймає один параметр: date — рядок, що представляє дату у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09').
# Функція повертає ціле число, яке вказує на кількість днів від заданої дати до поточної. Якщо задана дата пізніша за поточну, результат має бути від'ємним.
def get_days_from_today(days):
    # Обробка винятків: функція має впоратися з неправильним форматом вхідних даних. ("впоратися" не визначено, тому в цьому випадку те, що вона видасть exception вважається за "впоралась")
    day_ordinal = datetime.datetime.strptime(days, "%Y-%m-%d").toordinal()
    today_ordinal = datetime.datetime.today().toordinal()
    return today_ordinal - day_ordinal
    
print(get_days_from_today("2026-03-04"))