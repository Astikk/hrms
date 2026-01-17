from django.shortcuts import render
from rest_framework import generics
from .models import Attendance
from .serializers import AttendanceSerializer

# Create your views here.
class AttendanceCreateView(generics.CreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class AttendanceListView(generics.ListAPIView):
    serializer_class = AttendanceSerializer
    lookup_field = 'employee_id'

    def get_queryset(self):
        employee_id = self.kwargs['employee_id']
        return Attendance.objects.filter(employee_id=employee_id)
