from rest_framework import serializers
from apps.equipments.models import Equipment
from apps.accounts.models import User
from django.db import transaction


class EquipmentSerializer(serializers.ModelSerializer):
    created_by_email = serializers.EmailField(write_only=True, required=False)
    
    class Meta:
        model = Equipment
        fields = ['id', 'name', 'type', 'quantity', 'location', 'created_by', 'last_updated', 'created_by_email']
        read_only_fields = ['created_by', 'last_updated']
    
    def create(self, validated_data):
        email = validated_data.pop('created_by_email', None)
        
        with transaction.atomic():
            # If email is provided, find the user or create one
            if email:
                user, _ = User.objects.get_or_create(email=email, 
                                                   defaults={'is_active': True})
                validated_data['created_by'] = user
            else:
                # Use request user if no email provided
                validated_data['created_by'] = self.context['request'].user
                
            return super().create(validated_data)