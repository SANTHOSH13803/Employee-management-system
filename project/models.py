from django.db import models

class DesingnationTypes(models.Model):
    role_name = models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.role_name

class Employee(models.Model):
    empId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,null=True,blank=True)
    address = models.CharField(max_length=200,null=True,blank=True)
    city = models.CharField(max_length=50,null=True,blank=True)
    country = models.CharField(max_length=50,null=True,blank=True)
    zipcode = models.IntegerField()
    state = models.CharField(max_length=50,null=True,blank=True)
    designation = models.ForeignKey(DesingnationTypes,on_delete=models.CASCADE,default='0')
    date_of_joining = models.DateField(blank=True,null=True)
    date_of_birth = models.DateField(blank=True,null=True)
    active_field = models.BooleanField()
    leave_count = models.IntegerField(default=0,null=True)
    on_leave = models.BooleanField(default=False)

# class Test(models.Model):
#     empId = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=50,null=True,blank=True)
#     address = models.CharField(max_length=200,null=True,blank=True)
#     city = models.CharField(max_length=50,null=True,blank=True)
#     country = models.CharField(max_length=50,null=True,blank=True)
#     zipcode = models.IntegerField()
#     state = models.CharField(max_length=50,null=True,blank=True)
#     designation = models.ForeignKey(DesingnationTypes,on_delete=models.CASCADE,default='0')
#     date_of_joining = models.DateField(blank=True,null=True)
#     date_of_birth = models.DateField(blank=True,null=True)
#     active_field = models.BooleanField()
#     leave_count = models.IntegerField(default=0,null=True)
#     on_leave = models.BooleanField(default=False)