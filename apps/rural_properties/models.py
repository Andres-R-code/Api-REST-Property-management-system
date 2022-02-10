import uuid
from django.db import models


from apps.owners.models import LandOwner

class RuralProperty(models.Model):

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
        related_name='RuralProperty',
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


    name = models.CharField(
        unique = True,
        max_length=400, 
        blank = False, 
        null = False
        )

    tipe = models.CharField(
        blank = False, 
        null = False, 
        default = 'Rural',
        max_length = 5,
        editable = False
        )


    created = models.DateField(auto_now_add = True, auto_now = False)
    modified = models.DateField(auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = 'Rural Property'
        verbose_name_plural = 'Rural Properties'

    def __str__(self):
        return f'cadastral: {self.id_cadastral} registration_real_estate: {self.registration_real_estate} name: {self.name} owners: {self.owners} tipe: {self.tipe}'
