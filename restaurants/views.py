from django.core.cache import cache
from rest_framework import status, permissions, viewsets
from rest_framework.response import Response

from .models import Restaurant
from .serializers import RestaurantListSerializer, RestaurantCreateSerializer

class RestaurantView(viewsets.ModelViewSet):
    queryset = Restaurant.objects.select_related('owner').all()
    serializer_class = RestaurantListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'create':
            return RestaurantCreateSerializer
        return super().get_serializer_class()

    def list(self, request, *args, **kwargs):
        cache_key = 'restaurants'
        if cache_key in cache:
            return Response(cache.get(cache_key))

        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        cache.set(cache_key, serializer.data, 60 * 5)
        return Response(serializer.data)


