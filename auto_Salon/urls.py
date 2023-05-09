from django.urls import path, include
from .views import *

# from django.views.generic import TemplateView

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'car', CarViewSet, basename='car')
router.register(r'create', CreateViewSet,basename='create')
router.register(r'stamp', StampViewSet,basename='stamp')
router.register(r'country', CountryViewSet,basename='country')
router.register(r'releasedate', ReleasedateViewSet,basename='releasedate')
router.register(r'fuel', FuelViewSet,basename='fuel')
router.register(r'typeofcar', TypeofcarViewSet,basename='typeofcar')


urlpatterns = [
    path('api/', include(router.urls)),
    path('api-token-auth', AuthTokenView.as_view(), name='api_token_auth'),
    path('api-token-authout/', AuthTokenViewOut.as_view(), name='api_auth'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('createlist/', CreateListApiviews.as_view(), name='createlist'),
]