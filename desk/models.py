from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
import datetime


# Create your models here.
class User(AbstractUser):
    joindate = models.DateField(default=datetime.date.today())
    enddate = models.DateField(null=True)


class College(models.Model):
    name = models.CharField(max_length=30)
    address = models.TextField(max_length=100)
    city = models.CharField(max_length=20)
    pin_code = models.IntegerField()

    def __str__(self):
        return self.name


GENDER = [('Male', 'Male'), ('Female', 'Female')]


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    enroll_no = models.IntegerField()
    name = models.CharField(max_length=20)
    clg_id = models.ForeignKey(College, on_delete=models.SET_NULL, null=True)
    address = models.TextField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER)
    city = models.CharField(max_length=20)
    field = models.CharField(max_length=50)
    semester = models.IntegerField()

    def __str__(self):
        return str(self.enroll_no)

    @staticmethod
    def get_student_by_user(user):
        try:
            return Student.objects.get(user=user)
        except:
            False



CATEGORY = [('Canteen', 'Canteen'),
            ('Ground', 'Ground'),
            ('Com_lab', 'com_lab'),
            ('Faculty', 'Faculty'),
            ('ClassRoom', 'ClassRoom'),
            ('Library', 'Library'),
            ('Garden', 'Garden'),
            ('Parking', 'Parking'),
            ('Clg_bus', 'Clg_bus')]


class Complain(models.Model):
    std_id = models.ForeignKey(User,on_delete=models.CASCADE)
    type = models.CharField(choices=CATEGORY, max_length=20)
    date = models.DateField(auto_now_add=True)
    message = models.TextField(max_length=100)
    img = models.FileField()

    def __str__(self):
        return self.type





class Feedback(models.Model):
    std_id = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    feed = models.TextField(max_length=100)
    date = models.DateField(auto_now_add=True)
    happy = models.BooleanField()
    sad = models.BooleanField()
    
    # def __str__(self):
    #     return self.clg_id
