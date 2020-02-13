from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.CustUser)
# admin.site.register(models.Employee)
admin.site.register(models.Project)
admin.site.register(models.Category)
admin.site.register(models.ProjectTask)

