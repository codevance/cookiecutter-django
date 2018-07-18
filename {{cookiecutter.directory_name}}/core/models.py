from django.db import models
from utils.models import Base
from django.contrib.auth.models import User


class Profile(Base):
    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfis'

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return "perfil do usuário {}".format(self.user)

