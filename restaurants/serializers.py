from rest_framework import serializers
from .models import Restaurant

class RestaurantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name']


class RestaurantCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ["name", "address", "phone_number", "cover_photo"]

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['owner'] = user
        return super().create(validated_data)

class RestaurantDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ["id"]

    def delete(self, instance):
        instance.delete()
        return instance