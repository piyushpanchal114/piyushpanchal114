from django.urls import path
from . import views

urlpatterns = [
    path('plans/', views.plan_list),
    path('plans/<int:id>', views.plan_detail),
    path('transaction/', views.transaction)
]
