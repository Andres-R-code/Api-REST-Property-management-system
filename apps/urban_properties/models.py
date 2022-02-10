import uuid
from django.db import models


from apps.owners.models import LandOwner

class UrbanProperty(models.Model):

    code = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False
        )

    id_cadastral = models.CharField(
        max_length = 25,
        unique = True,
        null=True
        )

    registration_real_estate = models.CharField(
        max_length = 8,
        unique = True,
        null=True
        )

    owners = models.ManyToManyField(
        LandOwner, 
        related_name='UrbanProperty',
        blank = True, 
        null = True, 
    )

    country = models.CharField(
        max_length = 200, 
        blank = False, 
        null = False, 
        default = 'Colombia'
        )

    department = models.CharField(
        max_length = 300, 
        blank = False, 
        null = False
        )

    city = models.CharField(
        max_length = 300, 
        blank = False, 
        null = False
        )

    address = models.CharField(
        unique = True,
        max_length=300, 
        blank = False, 
        null = False
        )

    tipe = models.CharField(
        blank = False, 
        null = False, 
        default = 'Urban',
        max_length = 5,
        editable = False
        )


    created = models.DateField(auto_now_add = True, auto_now = False)
    modified = models.DateField(auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = 'Urban Property'
        verbose_name_plural = 'Urban Properties'

    def __str__(self):
        return f'cadastral: {self.id_cadastral} registration_real_estate: {self.registration_real_estate} address: {self.address} owners: {self.owners} tipe: {self.tipe}'

