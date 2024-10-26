from django.db import models
# from students.models import Student
# from teachers.models import Teacher
# Create your models here.


# Sinflar (Classes)
class Class(models.Model):
    name = models.CharField(max_length=50)  # Sinf nomi (masalan, 1-A, 2-B)
    class_teacher = models.ForeignKey('teachers.Teacher', on_delete=models.SET_NULL, null=True, related_name='classes')  # Sinf rahbari

    def __str__(self):
        return self.name
    

# Fanlar (Subjects)
class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    teachers = models.ManyToManyField('teachers.Teacher', related_name='teaches')

    def __str__(self):
        return self.name
    


# To'garaklar (Clubs)
class Club(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    students = models.ManyToManyField('students.Student', related_name='clubs')
    teacher = models.ForeignKey('teachers.Teacher', on_delete=models.SET_NULL, null=True)  # To'garakka mas'ul o'qituvchi

    def __str__(self):
        return self.name
    


# Yangiliklar (News)
class News(models.Model):
    title = models.CharField("sarlavha",max_length=200)
    content = models.TextField("yangilik haqida batafsil ma'lumot")
    image = models.ImageField('yangilik rasmi',upload_to="uploads/news/%Y/%m/%d")
    published_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    


# Bloglar (Blogs)
class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey('teachers.Teacher', on_delete=models.CASCADE)  # Blogni yozgan o'qituvchi
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    



    