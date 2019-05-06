from rest_framework import serializers

from .models import SwitchVendor, SwitchModel, UserPlace, User


class SwitchVendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SwitchVendor
        fields = ('id', 'title')


class UserPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPlace
        fields = ('id', 'street', 'ip', 'mac', 'active')


class SwitchModelSerializer(serializers.ModelSerializer):
    switch_vendor = serializers.CharField(source='switch_vendor.title')
    user_place = UserPlaceSerializer()

    class Meta:
        model = SwitchModel
        fields = ('id', 'switch_vendor', 'title', 'ports', 'user_place')
        ordering = ('id', )


class UserSerializer(serializers.ModelSerializer):
    installation_place = UserPlaceSerializer(read_only=True)
    installation_place_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'last_name', 'first_name', 'flat', 'installation_place', 'installation_place_id')

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user
