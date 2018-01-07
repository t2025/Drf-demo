from rest_framework import serializers
from webapp.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=('firstname','lastname')

        def create(self, validated_data):
           emp= Employee.objects.create(firstname=validated_data['firstname'],lastname=validated_data['lastname'] )
           emp.save()
           return emp
        