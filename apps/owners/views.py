from rest_framework.viewsets import ModelViewSet
from apps.owners.models import LandOwner
from apps.owners.serializers import CreateOwnerSerializer, GetIdOwnerSerializers, OwnersSerializers, UpdateOwnerSerializer


class OwnerViewSet(ModelViewSet):

    queryset = LandOwner.objects.all()
    serializer_class = OwnersSerializers


    def get_queryset(self):
        data = {}
        for k, v in self.request.query_params.items():
            data[k] = v
        return self.queryset.filter(**data)


    def get_serializer_class(self):

        if self.request.method == 'GET':
            return GetIdOwnerSerializers

        if self.request.method == 'POST':
            return CreateOwnerSerializer

        if self.request.method == 'PATCH':
            return UpdateOwnerSerializer
