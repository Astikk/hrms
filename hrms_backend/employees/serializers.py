from rest_framework import serializers
from .models import Employee
from attendance.serializers import AttendanceSerializer

class EmployeeSerializer(serializers.ModelSerializer):
    attendance = AttendanceSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'
