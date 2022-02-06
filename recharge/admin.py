from django.contrib import admin
from . models import Transaction, MobileOperator, Plan

# Register your models here.
admin.site.register(Transaction)
admin.site.register(MobileOperator)
admin.site.register(Plan)
