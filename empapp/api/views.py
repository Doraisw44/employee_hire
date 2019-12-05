from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from empapp.api.serializers import employees_serializers,departments_serializers,dept_emp_serializers,Title_serializers,salaries_serializers
from empapp.models import employees,departments,dept_emp,titles,salaries
# Create your views here.
class employee_list_crteate(ListCreateAPIView):
    queryset=employees.objects.all()
    serializer_class=employees_serializers
class employees_retrive(RetrieveUpdateDestroyAPIView):
    queryset=employees.objects.all()
    serializer_class=employees_serializers
class departments_list_crteate(ListCreateAPIView):
    queryset=departments.objects.all()
    serializer_class=departments_serializers
class departments_listcrtview(RetrieveUpdateDestroyAPIView):
    queryset=departments.objects.all()
    serializer_class=departments_serializers
    lookup_field='dept_no'
class dept_emp_listcreateview(ListCreateAPIView):
    queryset=dept_emp.objects.all()
    serializer_class=dept_emp_serializers
class Title_list_create(ListCreateAPIView):
    queryset=titles.objects.all()
    serializer_class=Title_serializers
class salaries_list_create(ListCreateAPIView):
    queryset=salaries.objects.all()
    serializer_class=salaries_serializers
