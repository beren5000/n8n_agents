from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from apps.accounts.models import User
from apps.accounts.api.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing warehouse equipment.
    
    list:
    Return a list of all equipment, filterable by name, user email, type, and location.
    Can be ordered by last_updated.
    
    create:
    Create a new equipment item. Can assign to a user if exists by providing an email address.

    Update:
    Update a new equipment item. Can assign to a user if exists by providing an email address.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {
        'email': ['icontains'],
    }
    search_fields = ['email', 'first_name', 'last_name']
    ordering_fields = ['id', 'email', 'first_name', 'last_name']
    ordering = ['-id']
    page_size_query_param = 'page_size'
    page_size = 10