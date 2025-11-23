from django.db import models

# Create your models here.\

class Event(models.Model):
    title = models.TextField(max_length=250)
    location = models.TextField(max_length=250)
    picture = models.ImageField(upload_to='images/', blank=True, null=False)
    date = models.DateTimeField()
     
    class Meta:
        ordering = ['-date']

    
    def __str__(self):
        return self.title
    

