from django.db import models
from  django.shortcuts import  reverse
# Create your models here.

""" models.Model 

    functions ---> apply queries , =-> objects.all() --> select * 
        --> create() ---> insert 
        --> delete() ---> delete 
        
    datatypes ---> corresponding dbms datatypes
"""

""" 
    id , name, email, grade , created_at , updated_at , 
    
    "create table --- > via models -- columns are not null unless you say something else"
"""

from departments.models import  Department
class Student(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    grade= models.IntegerField(default=0)
    image = models.ImageField(upload_to='students/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    dept = models.ForeignKey(Department, null=True, blank=True,
                             on_delete=models.CASCADE, related_name='dept_students')

    def __str__(self):
        return self.name

    @classmethod
    def get_all_students(cls):
        return cls.objects.all()



    @classmethod
    def get_student(cls, id):
        return cls.objects.get(id=id)

    def get_delete_url(self):
        # to return with url related to specific url name
        delete_url = reverse('students.delete',args=[self.id])
        return delete_url

    def get_show_url(self):
        show_url = reverse('students.show',args=[self.id])
        return show_url


    def get_image_url(self):
        return f"/media/{self.image}"


    def get_edit_url(self):
        edit_url = reverse('students.edit',args=[self.id])
        return edit_url


