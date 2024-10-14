from django.db import models

from root.app_utils.meta_models import MetaModel

# Create your models here.


class BloodGroups(MetaModel):
    name = models.CharField(max_length=5)
    codename = models.CharField(max_length=10)

    class Meta:
        db_table = 'blood_groups'
        verbose_name = 'Blood group'

    def __str__(self) -> str: return self.name


class Roles(MetaModel):
    name = models.CharField(max_length=20)
    codename = models.CharField(max_length=20)

    class Meta:
        db_table = 'roles'
        verbose_name = 'role'

    def __str__(self) -> str: return self.name
