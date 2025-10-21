from datetime import datetime, date, timedelta

def get_upcoming_birthdays(users, today=None):

    today = today or date.today()
    in_7_days = today + timedelta(days=7)
    result = []

    for user in users:
        bday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # B-day in current year
        bday_this_year = bday.replace(year=today.year)

        # If bday is passed already - take next year
        target_bday = bday_this_year if bday_this_year >= today else (
            bday.replace(year=today.year + 1) if not (bday.month == 2 and bday.day == 29)
            else date(today.year + 1, 3, 1)
        )

        
        if today <= target_bday <= in_7_days:
            congratulation_date = target_bday
            
            
            shift = (7 - congratulation_date.weekday()) % 7  # Shift from weekday to monday
            
            if shift in (1, 2):
                congratulation_date += timedelta(days=shift)

            result.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return result

users = [
    {"name": "John Doe", "birthday": "1985.10.28"},
    {"name": "Jane Smith", "birthday": "1990.10.27"}
]


upcoming_birthdays = get_upcoming_birthdays(users)

print("Список привітань на цьому тижні:", upcoming_birthdays)