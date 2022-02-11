from rest_framework.viewsets import ModelViewSet
from apps.urban_properties.models import UrbanProperty
from apps.urban_properties.serializers import UrbanPropertySerializers

class UrbanPropertieViewSet(ModelViewSet):

    queryset = UrbanProperty.objects.all()
    serializer_class = UrbanPropertySerializers


    def get_queryset(self):
        data = {}
        for k, v in self.request.query_params.items():
            data[k] = v
        return self.queryset.filter(**data)
