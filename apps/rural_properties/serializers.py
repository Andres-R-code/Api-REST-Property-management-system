
from rest_framework.serializers import ModelSerializer
from apps.owners.serializers import OwnersSerializers
from apps.rural_properties.models import RuralProperty


class RuralPropertySerializers(ModelSerializer):

    owners =  OwnersSerializers(many = True)

    class Meta:
        model = RuralProperty
        fields = (
            'code', 
            'id_cadastral',
            'registration_real_estate',
            'owners',
            'country',
            'department',
            'name',
            'tipe'
        )