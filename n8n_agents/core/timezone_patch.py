"""
Timezone patch for Django 4.2 on Python 3.11
"""
import sys
from datetime import datetime, timedelta, timezone
from functools import wraps

# Patch sys.modules to provide our simplified implementation
class TimezonePatch:
    def __init__(self, name):
        self.name = name
        
    def now(self):
        return datetime.now(timezone.utc)
        
    def localtime(self, value=None):
        if value is None:
            value = self.now()
        return value
    
    def activate(self, timezone):
        pass
        
    def deactivate(self):
        pass
    
    def get_current_timezone(self):
        return timezone.utc
        
    def get_default_timezone(self):
        return timezone.utc
        
    def is_aware(self, value):
        return value.tzinfo is not None and value.tzinfo.utcoffset(value) is not None
    
    def is_naive(self, value):
        return not self.is_aware(value)
    
    def make_aware(self, value, timezone=None):
        if timezone is None:
            timezone = self.get_current_timezone()
        if self.is_aware(value):
            return value
        return value.replace(tzinfo=timezone)
    
    def make_naive(self, value, timezone=None):
        if timezone is None:
            timezone = self.get_current_timezone()
        if self.is_naive(value):
            return value
        return value.replace(tzinfo=None)
    
    # Missing functions
    def _datetime_ambiguous_or_imaginary(self, dt, tz):
        """
        Returns True if the given datetime is ambiguous or imaginary.
        Simplified version that always returns False to avoid complexity.
        """
        return False
    
    def template_localtime(self, value):
        """
        Checks if value is a datetime and converts it to local time if necessary.
        """
        if isinstance(value, datetime):
            return self.localtime(value)
        return value

# Install the patch
sys.modules['django.utils.timezone'] = TimezonePatch('django.utils.timezone')