# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from webapp.models import Employee
from webapp.serializer import EmployeeSerializer

@api_view(['POST'])
def employee_view(request):
    serializer=EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_created)
    else:
        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
