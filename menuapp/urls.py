from debug_toolbar.toolbar import debug_toolbar_urls
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.response import Response
from .views import MenuCategoryViewSet, DishViewSet, IngredientViewSet
from restaurants.views import RestaurantView
from accounts.views import UserRegistrationView


class CustomRouter(DefaultRouter):
    def get_api_root_view(self, *args, **kwargs):
        api_root_view = super().get_api_root_view(*args, **kwargs)

        def view(request, *args, **kwargs):
            response = api_root_view(request, *args, **kwargs)
            if isinstance(response, Response) and 'register' not in response.data:
                response.data['register'] = request.build_absolute_uri('register/')
            return response

        return view


router = CustomRouter()
router.register(r'categories', MenuCategoryViewSet, basename='categories')
router.register(r'subcategories', MenuCategoryViewSet, basename='subcategories')
router.register(r'dishes', DishViewSet, basename='dishes')
router.register(r'ingredients', IngredientViewSet, basename='ingredients')
router.register(r'restaurants', RestaurantView, basename='restaurant')
urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationView.as_view(), name='register'),
]
