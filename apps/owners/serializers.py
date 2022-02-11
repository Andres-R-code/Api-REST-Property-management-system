from apps.owners.models import LandOwner
from rest_framework.serializers import ModelSerializer

class OwnersSerializers(ModelSerializer):

    class Meta:
        model = LandOwner
        fields = (
            'code', 
            'id_owner',
            'tipe_owner',
            'names',
            'last_name',
            'email',
            'country',
            'department',
            'city',
            'address'
        )

class CreateOwnerSerializer(ModelSerializer):

    class Meta:
        model = LandOwner
        fields = (
            'id_owner',
            'tipe_owner',
            'names',
            'last_name',
            'email',
            'country',
            'department',
            'city',
            'address'
        )
    
    def create(self, validated_data):
        land_owner = LandOwner.objects.create(
            **validated_data,
        )
        land_owner.save()
        return land_owner

class GetIdOwnerSerializers(ModelSerializer):

    class Meta:
        model = LandOwner
        fields = (
            'code', 
            'id_owner',
            'tipe_owner',
            'names',
            'last_name',
            'email',
            'country',
            'department',
            'city',
            'address'
        )

class UpdateOwnerSerializer(ModelSerializer):

    class Meta:
        model = LandOwner
        fields = (
            'id_owner',
            'tipe_owner',
            'names',
            'last_name',
            'email',
            'country',
            'department',
            'city',
            'address'
        )

