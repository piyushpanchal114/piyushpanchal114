from django.db import models

# Create your models here.
class MobileOperator(models.Model):
    operator_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


class Plan(models.Model):
    plan_name = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.IntegerField()
    validity = models.CharField(max_length=255)
    operator_name = models.ForeignKey(MobileOperator, on_delete=models.PROTECT)


class Transaction(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed'),
    ]

    transaction_id = models.AutoField(primary_key=True)
    mobile_number = models.CharField(max_length=10)
    operator_name = models.ForeignKey(MobileOperator, on_delete=models.PROTECT)
    amount = models.ForeignKey(Plan, on_delete=models.PROTECT)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)
    transaction_date = models.DateTimeField(auto_now=True)
