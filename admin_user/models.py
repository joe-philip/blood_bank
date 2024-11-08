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


class Countries(MetaModel):
    common_name = models.CharField(max_length=50)
    official_name = models.CharField(max_length=250)
    iso2 = models.CharField(max_length=2)
    iso3 = models.CharField(max_length=3)
    CIOC_DESCRIPTION = 'Code of the International Olympic Committee'
    cioc = models.CharField(
        db_comment=CIOC_DESCRIPTION,
        help_text=CIOC_DESCRIPTION
    )
    flag = models.CharField(max_length=5)
    timezones = models.JSONField(default=dict)
    pincode_regex = models.CharField(max_length=10)
    phone_codes = models.JSONField(default=dict)

    class Meta:
        db_table = 'countries'
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self) -> str:
        return self.common_name
