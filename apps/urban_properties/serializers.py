
from rest_framework.serializers import ModelSerializer
from apps.urban_properties.models import UrbanProperty


class UrbanPropertySerializers(ModelSerializer):

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