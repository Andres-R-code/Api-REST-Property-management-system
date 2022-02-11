from django.contrib.auth.models import User
from rest_framework import status

from rest_framework.response import Response
from apps.users.models import UserCustom
from apps.users.permissions import UserPermissions

from apps.users.serializers import GetUsersSerializers, CreateUserSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

class UserViewSet(ModelViewSet):

    queryset = UserCustom.objects.all()
    serializer_class = GetUsersSerializers
    permission_classes = (UserPermissions,)
    pagination_class = None

    def get_serializer_class(self):

        if self.request.method == 'GET':
            return  GetUsersSerializers


        if self.request.method == 'POST':
            return CreateUserSerializer

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer_class()
        serialized = serializer(data=request.data)

        if not serialized.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serialized.errors)
        serialized.save()
        
        return Response(status=status.HTTP_201_CREATED, data=serialized.data)