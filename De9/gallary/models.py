from django.db import models

# Create your models here.
class Gallary(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', max_length=200, null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering =['-created']

    def __str__(self):
        return self.title


 