from django.forms import ValidationError
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
        

    def to_representation(self, instance):
        """Override to_representation to show email instead of ID for created_by"""
        ret = super().to_representation(instance)
        # Replace user ID with user email
        if instance.created_by:
            ret['created_by'] = instance.created_by.email
        return ret
    
    def create(self, validated_data):
        email = validated_data.pop('created_by_email', None)
        
        with transaction.atomic():
            if email:
                try:
                    # Single query to get user or raise exception
                    user = User.objects.get(email=email)
                    validated_data['created_by'] = user
                except User.DoesNotExist:
                    raise ValidationError({'created_by_email': f"User with email '{email}' does not exist."})
            else:
                # Use request user if no email provided
                validated_data['created_by'] = self.context['request'].user
                
            return super().create(validated_data)
    
    def update(self, instance, validated_data):
        """Handle updating equipment, including changing the created_by user if email provided"""
        email = validated_data.pop('created_by_email', None)
        
        if email:
            with transaction.atomic():
                try:
                    # Single query to get user or raise exception
                    user = User.objects.get(email=email)
                    validated_data['created_by'] = user
                except User.DoesNotExist:
                    raise ValidationError({'created_by_email': f"User with email '{email}' does not exist."})
        
        # Update other fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
            
        instance.save()
        return instance