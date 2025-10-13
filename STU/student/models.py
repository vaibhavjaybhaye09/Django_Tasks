from django.db import models

# Create your models here.
class Student(models.Model):
    class Course(models.TextChoices):
        PYTHON ='PY',' Python'
        JAVA = 'JA','Java'
        DJANGO = 'DJ','django'
        

       

    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    course = models.CharField(max_length=5,choices=Course.choices, default=Course.PYTHON)
    created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created']
    
