from rest_framework import serializers
from .models import employee
#converts the model into json format data
class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=employee
        #returns all the fields as response when we ask for employee id, any particular field could also be returned.
        #fields=('f_name')
        fields='__all__'
