from django.test import TestCase
from model_bakery import baker


class ModelTestCase(TestCase):
    def test_model_profile(self):
        user = baker.make('User')
        assert user.profile is not None
