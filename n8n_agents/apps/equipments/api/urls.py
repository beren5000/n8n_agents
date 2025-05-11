from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.equipments.api.views import EquipmentViewSet

router = DefaultRouter()
router.register(r'equipments', EquipmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]