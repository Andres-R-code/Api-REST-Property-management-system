
from rest_framework.serializers import ModelSerializer
from apps.owners.serializers import OwnersSerializers
from apps.urban_properties.models import UrbanProperty


class UrbanPropertySerializers(ModelSerializer):

    owners =  OwnersSerializers(many = True)

    class Meta:
        model = UrbanProperty
        fields = (
            'code', 
            'id_cadastral',
            'registration_real_estate',
            'owners',
            'country',
            'department',
            'city',
            'address',
            'tipe'
        )