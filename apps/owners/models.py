import uuid
from django.db import models


VISIVILITY_CHOICES_TIPE_OWNER = [
    ('PERSON', 'person'),
    ('COMPANY', 'company')
] 


class LandOwner(models.Model):

    code = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False
        )

    id_owner = models.CharField(
        max_length = 10,
        unique = True,
        null=True
        )

    tipe_owner = models.CharField(
        choices = VISIVILITY_CHOICES_TIPE_OWNER,
        max_length = 7,
        )
    names = models.CharField(
        max_length = 100, 
        blank = False, 
        null = False
        )
    last_name = models.CharField(
        max_length = 100, 
        blank = True, 
        null = True
        )
    email = models.EmailField(
        unique = True,
        max_length = 100, 
        blank = False, 
        null = False
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

    created = models.DateField(auto_now_add = True, auto_now = False)
    modified = models.DateField(auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = 'Land Owners'
        verbose_name_plural = 'Land Owners'

    def __str__(self):
        return f'id: {self.id_owner} names{self.names} {self.last_name} address: {self.address} code: {self.code} '

