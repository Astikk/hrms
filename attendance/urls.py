from django.urls import path
from .views import AttendanceCreateView, AttendanceListView

urlpatterns = [
    path('attendance/', AttendanceCreateView.as_view(), name='attendance-create'),
    path('attendance/<int:employee_id>/', AttendanceListView.as_view(), name='attendance-list'),
]
