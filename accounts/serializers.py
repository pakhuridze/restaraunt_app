from rest_framework import serializers
from accounts.models import CustomUser


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'contact_number', 'password')

    def create(self, validated_data):

        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            contact_number=validated_data['contact_number'],
            password=validated_data['password']
        )
        return user