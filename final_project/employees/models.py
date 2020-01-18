from django.db import models

# Create your models here.

class Employees(models.Model):
    employee_id = models.AutoField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=15)
    hire_date = models.DateField()
    job_id = models.IntegerField()
    salary = models.FloatField()
    commission_pct = models.FloatField()
    manager_id = models.IntegerField()
    department_id = models.IntegerField()

    def __str__(self):
        return self.name

class Departments(models.Model):
    department_id = models.AutoField()
    department_name = models.CharField(max_length=50)
    department_manager_id = models.IntegerField()

class Jobs(models.Model):
    job_id = models.AutoField()
    job_name = models.CharField(max_length=50)
    job_description = models.CharField(max_length=250)

    def __str__(self):
        return self.name
