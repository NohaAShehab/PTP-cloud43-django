from django.db import models
from django.shortcuts import reverse
# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


    @classmethod
    def get_all_departments(cls):
        return cls.objects.all()

    @classmethod
    def get_specific_department(cls, id):
        return cls.objects.get(id=id)

    def get_show_url(self):
        url = reverse('departments.show', args=[self.id])
        return url

    def get_delete_url(self):
        url = reverse('departments.delete', args=[self.id])
        return url