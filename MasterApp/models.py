from django.db import models
from django.contrib.auth.models import AbstractUser

class CustUser(AbstractUser):
    Name = models.CharField(max_length=200,null=True,blank=True)
    Mobile = models.CharField(max_length=15,null=True,blank=True)
    Type = models.ForeignKey('MasterApp.Category',on_delete=models.CASCADE,null=True,blank=True)
    is_employee = models.BooleanField(default=False,null=True,blank=True)


class Project(models.Model):
    Name = models.CharField(max_length=200,null=True,blank=True)
    Start_Date = models.DateField(null=True,blank=True)
    End_Date = models.DateField(null=True,blank=True)
    Category = models.ForeignKey('MasterApp.Category',on_delete=models.CASCADE,null=True,blank=True)
    Flage = models.BooleanField(default=True,null=True,blank=True)

class Category(models.Model):
    Project_Category = models.CharField(max_length=200,null=True,blank=True)
    Employee_Category = models.CharField(max_length=200,null=True,blank=True)
    P = models.BooleanField(default=False)
    E = models.BooleanField(default=False)

class ProjectTask(models.Model):
    ProjectName = models.ForeignKey('MasterApp.Project',on_delete=models.CASCADE,null=True,blank=True)
    Priority = models.IntegerField(null=True,blank=True)
    TeamLeader = models.ForeignKey('MasterApp.CustUser',related_name='teamleader',on_delete=models.CASCADE,null=True,blank=True)
    ProjectEmployee = models.ForeignKey('MasterApp.CustUser',related_name='projectemployee',on_delete=models.CASCADE,null=True,blank=True)
    Task = models.CharField(max_length=200,null=True,blank=True)
    Task_Due_date = models.DateField(null=True,blank=True)
    Task_Status = models.CharField(default='Not_Started',max_length=200,null=True,blank=True)
    Task_Discription = models.CharField(max_length=500,null=True,blank=True)
    PT = models.BooleanField(default=False)

class Issue(models.Model):
    ProjectName = models.ForeignKey('MasterApp.Project',related_name='issuename',on_delete=models.CASCADE,null=True,blank=True)
    ProjectEmployee = models.ForeignKey('MasterApp.CustUser', related_name='issueprojectemployee', on_delete=models.CASCADE,
                                        null=True, blank=True)
    Issue_Due_date = models.DateField(null=True, blank=True)
    Issue_Status = models.CharField(max_length=200, default='Not_Started', null=True, blank=True)
    Issues = models.CharField(max_length=500, default='No Issue', null=True, blank=True)
    PI = models.BooleanField(default=False)

class Menu(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50)

class Permissions(models.Model):
    Menu = models.ForeignKey(Menu,on_delete=models.CASCADE)
    Employee = models.ForeignKey(CustUser,on_delete=models.CASCADE)
    isView = models.BooleanField(default=False)
    isAdd = models.BooleanField(default=False)
    isEdit = models.BooleanField(default=False)
    isDelete = models.BooleanField(default=False)

class Industry(models.Model):
    industry = models.CharField(max_length=200,null=True,blank=True)


class Organisation(models.Model):
    Owner = models.CharField(max_length=200,null=True,blank=True)
    Contacted_Person = models.CharField(max_length=200,null=True,blank=True)
    Mobile = models.IntegerField(null=True,blank=True)
    Phone = models.IntegerField(null=True,blank=True)
    Email = models.EmailField(max_length=200,null=True,blank=True)
    Website = models.CharField(max_length=200,null=True,blank=True)
    Street = models.CharField(max_length=200,null=True,blank=True)
    Country = models.CharField(max_length=200,null=True,blank=True)
    State = models.CharField(max_length=200,null=True,blank=True)
    Description = models.CharField(max_length=200,null=True,blank=True)
    Fax = models.CharField(max_length=200,null=True,blank=True)
    Industry = models.ForeignKey('MasterApp.Industry',related_name='orgind',on_delete=models.CASCADE,null=True,blank=True)
    City = models.CharField(max_length=200,null=True,blank=True)
    Zipcode = models.IntegerField(null=True,blank=True)


class Products(models.Model):
    product = models.CharField(max_length=200,null=True,blank=True)


class Service(models.Model):
    service = models.CharField(max_length=200,null=True,blank=True)


class Lead(models.Model):
    Lead_Title = models.CharField(max_length=200,null=True,blank=True)
    Owner = models.ForeignKey('MasterApp.Organisation',related_name='owner',on_delete=models.CASCADE,null=True,blank=True)
    Contacted_Person = models.CharField(max_length=200,null=True,blank=True)
    Phone = models.IntegerField(null=True,blank=True)
    Purpose = models.CharField(max_length=200,null=True,blank=True)
    Priority = models.CharField(max_length=200,null=True,blank=True)
    Annual_Revenue = models.IntegerField(null=True,blank=True)
    Description = models.CharField(max_length=200,null=True,blank=True)
    Date = models.DateField(null=True,blank=True)
    Industry = models.ForeignKey('MasterApp.Industry',related_name='leadindustry',on_delete=models.CASCADE,null=True,blank=True)
    Mobile = models.ForeignKey('MasterApp.Organisation',related_name='mobile',on_delete=models.CASCADE,null=True,blank=True)
    Email = models.EmailField(null=True,blank=True)
    Lead_Status = models.CharField(max_length=200,null=True,blank=True)
    Sales_Employee = models.CharField(max_length=200,null=True,blank=True)
    Lead_Source = models.CharField(max_length=200,null=True,blank=True)