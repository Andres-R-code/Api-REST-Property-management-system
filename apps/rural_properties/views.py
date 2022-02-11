from rest_framework.viewsets import ModelViewSet
from apps.rural_properties.models import RuralProperty
from apps.rural_properties.serializers import RuralPropertySerializers


class RuralPropertieViewSet(ModelViewSet):

    queryset = RuralProperty.objects.all()
    serializer_class = RuralPropertySerializers


    def get_queryset(self):
        data = {}
        for k, v in self.request.query_params.items():
            data[k] = v
        return self.queryset.filter(**data)
