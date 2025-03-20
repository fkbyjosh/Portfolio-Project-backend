from rest_framework import serializers
from .models import Policy

class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = ['policy_id', 'client_name', 'premium', 'payment_status', 'assigned_status', 'date_processed']
