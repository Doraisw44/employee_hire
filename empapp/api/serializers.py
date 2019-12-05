from rest_framework import serializers
from empapp.models import employees,departments,dept_emp,titles,salaries
from datetime import date

class dept_emp_serializers(serializers.ModelSerializer):
    class Meta:
        model=dept_emp
        fields='__all__'
class Title_serializers(serializers.ModelSerializer):
    def validate(self,data):
        title=data.get('title')
        if title in ['Senior Engineer','Staff Engineer','Senior Staff','Assistant Engineer','Technique Leader']:
            raise serializers.ValidationError({'no':'Hike'})
        return title
    class Meta:
        model=titles
        fields='__all__'
class salaries_serializers(serializers.ModelSerializer):
    class Meta:
        model=salaries
        fields='__all__'

class employees_serializers(serializers.ModelSerializer):
    emp_no_by_employees=dept_emp_serializers(read_only=True,many=True)
    titles_by_employees=Title_serializers(read_only=True,many=True)
    salaries_by_employees=salaries_serializers(read_only=True,many=True)
    def age_restriction(self,value):
        today=date.today()
        age=today.year-value.year
        value=age
        if value<60:
            raise serializers.ValidationError("your age is not matching")
        elif value<18:
            raise serializers.ValidationError("your age is not matching")

        return value
    class Meta:
        model=employees
        fields='__all__'
class departments_serializers(serializers.ModelSerializer):
    dept_no_by_departments=dept_emp_serializers(read_only=True,many=True)
    def validate(self,data):
        dept_name=data.get('dept_name')
        if dept_name in ['Customer Service','Development','Finance','Human resources','sales']:
            raise serializers.ValidationError({'no':'hike'})
        return dept_name
    class Meta:
        model=departments
        fields='__all__'
