from datetime import datetime


def cleaning_date_to_use_with_celery(day):
    if isinstance(day, str):
        if 'T' in day:
            day = day.split('T')[0]
        day = datetime.strptime(day, "%Y-%m-%d").date()

    if isinstance(day, datetime):
        day = day.date()

    return day
