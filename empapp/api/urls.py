from django.conf.urls import url,include
from empapp.api import views

urlpatterns = [
    url(r'^emp-api/$', views.employee_list_crteate.as_view()),
    url(r'^emp-api/(?P<pk>\d+)/$', views.employees_retrive.as_view()),
    url(r'^dept-api/$', views.departments_list_crteate.as_view()),
    url(r'^dept-api/(?P<dept_no>\w+)/$', views.departments_listcrtview.as_view()),
    url(r'^dept-emp-api/$', views.dept_emp_listcreateview.as_view()),
    url(r'^emp-title-api/$', views.Title_list_create.as_view()),
    url(r'^emp-sal-api/$', views.salaries_list_create.as_view()),

]
