from dataclasses import field
from rest_framework import serializers

from recharge.models import Transaction

class PlanSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    plan_name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    amount = serializers.IntegerField()
    validity = serializers.CharField(max_length=255)


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['transaction_id', 'mobile_number', 'operator_name', 'amount', 'payment_status', 'transaction_date']
  
    
     