#request an api and get the json in return
#default
from django.shortcuts import render
#return the response
from django.http import HttpResponse
#return the object or if not found then show 404
from django.shortcuts import get_object_or_404
#the normal views can return the api data
from rest_framework.views import APIView
#returns the response eg: 200,404,500
from rest_framework.response import Response
from rest_framework import status
from .models import employee
from .serializers import employeeSerializer
# Create your views here.

class employeelist(APIView):
    def get(self,request):
        emp1=employee.objects.all()
        #convert to json.
        serializer=employeeSerializer(emp1,many=True)
        return Response(serializer.data)
    def post(self):
        pass
