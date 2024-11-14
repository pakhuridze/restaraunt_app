from rest_framework import viewsets, permissions
from .models import MenuCategory, Dish, Ingredient
from .serializers import MenuCategorySerializer, MenuCategoryCreateSerializer, DishSerializer, IngredientSerializer, \
    IngredientCreateSerializer, SubMenuCategorySerializer


class MenuCategoryViewSet(viewsets.ModelViewSet):
    queryset = MenuCategory.objects.all()
    serializer_class = SubMenuCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return MenuCategoryCreateSerializer
        return super().get_serializer_class()

class SubMenuCategoryViewSet(viewsets.ModelViewSet):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = IngredientSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return IngredientCreateSerializer
        return super().get_serializer_class()