from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Plan
from .serializers import PlanSerializer, TransactionSerializer

@api_view()
def plan_list(request):
    queryset = Plan.objects.all()
    serializer = PlanSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def plan_detail(request, id):
    plan = get_object_or_404(Plan, pk=id)
    serializer = PlanSerializer(plan)
    return Response(serializer.data)


@api_view(['POST'])
def transaction(request):
    serializer = TransactionSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response('recharge done')