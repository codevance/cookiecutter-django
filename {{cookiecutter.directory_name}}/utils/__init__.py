from datetime import datetime


def cleaning_date_to_use_with_celery(day):
    if isinstance(day, str):
        if 'T' in day:
            day = day.split('T')[0]
        day = datetime.strptime(day, "%Y-%m-%d").date()

    if isinstance(day, datetime):
        day = day.date()

    return day


def create_logentry(creator, object, message=None, is_change=False):
    from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, ContentType

    if not message:
        message = 'Adicionado.'

    LogEntry.objects.log_action(
        user_id=creator.id,
        content_type_id=ContentType.objects.get_for_model(object).pk,
        object_id=object.id,
        object_repr=str(object),
        action_flag=CHANGE if is_change else ADDITION,
        change_message=message,
    )