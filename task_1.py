import datetime

def get_days_from_today(days):
    day_ordinal = datetime.datetime.strptime(days, "%Y-%m-%d").toordinal()
    today_ordinal = datetime.datetime.today().toordinal()
    return today_ordinal - day_ordinal

print(get_days_from_today("2026-03-04"))