from rest_framework import routers
from django.urls import path
from .api import EmployeeViewSet

# router = routers.DefaultRouter()
# router.register('/', EmployeeViewSet, 'employees')

# urlpatterns = [
#     path('', EmployeeViewSet,  name='employees')
#     # path('<int:product_id>/', views.product_detail, name='product_detail'),
#     # path('new/', views.new_product, name='new_product'),
# ]

# urlpatterns
# urlpatterns = router.urls


urlpatterns = [
    path('', EmployeeViewSet.as_view({'get': 'list', 'post': 'create'}), name='employees_list'),
    # path('<int:pk>/', EmployeeViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='employee_detail'),
]