
from rest_framework.serializers import ModelSerializer
from apps.rural_properties.models import RuralProperty

class RuralPropertySerializers(ModelSerializer):

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