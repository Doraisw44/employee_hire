from django.db import models

# Create your models here.
class employees(models.Model):
    emp_no=models.IntegerField(primary_key=True)
    birth_date=models.DateField(null=False)
    first_name=models.CharField(max_length=14)
    last_name=models.CharField(max_length=16)
    gender_choices=(
    ('male','M'),
    ('female','F')
    )
    gender=models.CharField(choices=gender_choices,max_length=6)
    hire_date=models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.emp_no
class departments(models.Model):
    dept_no=models.CharField(max_length=4,primary_key=True)
    dept_name=models.CharField(max_length=40,null=False)
    def __str__(self):
        return self.dept_no
class dept_emp(models.Model):
    emp_no=models.ForeignKey(employees,on_delete=models.CASCADE,related_name='emp_no_by_employees')
    dept_no=models.ForeignKey(departments,on_delete=models.CASCADE,related_name='dept_no_by_departments')
    from_date=models.DateField(null=False)
    to_date=models.DateField(null=False)
class titles(models.Model):
    emp_no=models.ForeignKey(employees,on_delete=models.CASCADE,related_name='titles_by_employees')
    title=models.CharField(max_length=50,primary_key=True)
    from_date=models.DateField()
    to_date=models.DateField()
class salaries(models.Model):
    emp_no=models.ForeignKey(employees,on_delete=models.CASCADE,related_name='salaries_by_employees')
    salary=models.FloatField()
    from_date=models.DateField()
    to_date=models.DateField()
