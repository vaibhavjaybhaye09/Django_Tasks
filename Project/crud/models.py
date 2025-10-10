from django.db import models

# Create your models here.
class Todo(models.Model):
    titel = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    complete = models.BooleanField(blank=True)
    pic = models.ImageField(upload_to='images/', max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.titel