from rest_framework import viewsets, permissions
from .models import Employee
from .serializers import EmployeeSerializer

# Employee Viewset


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EmployeeSerializer
