from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from apps.equipments.models import Equipment
from apps.equipments.api.serializers import EquipmentSerializer


class EquipmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing warehouse equipment.
    
    list:
    Return a list of all equipment, filterable by name, user email, type, and location.
    Can be ordered by last_updated.
    
    create:
    Create a new equipment item. Can assign to a user by providing an email address.
    """
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {
        'name': ['icontains'],
        'type': ['icontains'],
        'location': ['icontains'],
        'created_by__email': ['exact'],
    }
    search_fields = ['name', 'type', 'location']
    ordering_fields = ['name', 'type', 'quantity', 'location', 'last_updated']
    ordering = ['-last_updated']