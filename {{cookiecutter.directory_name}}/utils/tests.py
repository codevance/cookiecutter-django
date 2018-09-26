import pytest
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE
from model_mommy import mommy

from . import create_logentry


@pytest.mark.django_db
def test_create_logentry():
    user1 = mommy.make('User')
    user2 = mommy.make('User')

    assert not LogEntry.objects.all()

    create_logentry(creator=user1, object=user2)

    assert LogEntry.objects.all()
    logentry = LogEntry.objects.get(
        user=user1, object_id=user2.id, object_repr=str(user2), action_flag=ADDITION)
    assert logentry.change_message == 'Adicionado.'

    create_logentry(creator=user1, object=user2, is_change=True, message='Teste')
    logentry = LogEntry.objects.get(
        user=user1, object_id=user2.id, object_repr=str(user2), action_flag=CHANGE)
    assert logentry.change_message == 'Teste'
