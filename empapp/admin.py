from django.contrib import admin
from empapp.models import employees,departments,dept_emp,titles,salaries
# Register your models here.
admin.site.register(employees)
admin.site.register(departments)
admin.site.register(dept_emp)
admin.site.register(titles)
admin.site.register(salaries)
