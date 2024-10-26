from django.db import models
# from common.models import Class
# Create your models here.


# O'quvchilar (Students)
class Student(models.Model):
    full_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    student_class = models.ForeignKey("common.Class", on_delete=models.SET_NULL, null=True)  # O'quvchi sinfi
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    image = models.ImageField(upload_to='uploads/students/%Y/%m/%d')
    enrolled_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.full_name
    

# Cartalar (Certificates)
class Certificate(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  
    name = models.CharField(max_length=100)
    issued_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.student.full_name}"
