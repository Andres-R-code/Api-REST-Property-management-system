
from rest_framework.serializers import ModelSerializer
from apps.users.models import UserCustom

class GetUsersSerializers(ModelSerializer):

    class Meta:
        model = UserCustom
        fields = ( 
            'username',
        )

class CreateUserSerializer(ModelSerializer):

    class Meta:
        model = UserCustom
        fields = ('email', 'first_name', 'last_name','username', 'password')
    
    def create(self, validated_data):
        user = UserCustom.objects.create(
            **validated_data,

        )
        user.set_password(validated_data["password"])
        user.save()
        return user

