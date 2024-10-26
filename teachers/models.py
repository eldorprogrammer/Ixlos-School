from django.db import models
# from common.models import Subject
# Create your models here.


# O'qituvchilar (Teachers)
class Teacher(models.Model):
    full_name = models.CharField("O'qtuvchi ism familyasi",max_length=100)
    email = models.EmailField("emaili")
    phone = models.CharField('telefon raqami',max_length=20)
    subjects = models.ManyToManyField('common.Subject') 
    image = models.ImageField("o'qtuvchi rasmi", upload_to='uploads/teachers/%Y/%m/%d')
    body = models.TextField("o'qtuvchi haqida batafsil ma'lumot")
    information = models.CharField("ma'lumoti",max_length=100)
    experience_years = models.PositiveIntegerField()
    
    def __str__(self):
        return self.full_name