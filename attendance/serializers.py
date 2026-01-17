from rest_framework import serializers
from .models import Attendance

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'
    
    def validate(self, attrs):
        employee = attrs.get('employee')
        date = attrs.get('date')

        if Attendance.objects.filter(employee = employee, date = date).exists():
            raise serializers.ValidationError("Attendance already marked for this employee on this date.")
        return attrs
