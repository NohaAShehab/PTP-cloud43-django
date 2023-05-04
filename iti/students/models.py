from django.db import models

# Create your models here.

""" models.Model 

    functions ---> apply queries , =-> objects.all() --> select * 
        --> create() ---> insert 
        --> delete() ---> delete 
        
    datatypes ---> corresponding dbms datatypes
"""

""" 
    id , name, email, grade , created_at , updated_at , 
"""
class Student(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()
    grade= models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


