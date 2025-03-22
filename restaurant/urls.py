from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from restaurant.views import BookingViewSet
from .views import BookingViewSet, MenuViewSet

router = DefaultRouter()
router.register(r'bookings', BookingViewSet, basename='booking')
router.register(r'menu', MenuViewSet, basename='menu')

urlpatterns = [
    path('', include(router.urls)),  # Registers all API routes
]