from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'pk': self.pk})
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , related_name='profile')
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    website = models.URLField(blank=True)


    def __str__(self):
        return f"Profile of {self.user.username}"
    
    def get_absolute_url(self):
        return reverse('profile_detail', kwargs={'pk': self.pk})
    
class Tag(models.model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    featured_image = models.ImageField(upload_to='blog_images/', null=True, blank=True , help_text="Upload a featured image")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='blogs')
    tags = models.ManyToManyField(Tag, blank=True, related_name='blogs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    view = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-created_at']
        unique_together = ('title', 'author')

    
    
    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'pk': self.pk})
    

class Comment(models.Model):  
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')  
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')  
    content = models.TextField(max_length=1000) 
    created_at = models.DateTimeField(auto_now_add=True)  
    is_approved = models.BooleanField(default=True)  
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')  

    class Meta: 
        ordering = ['created_at']  

    def __str__(self):  
        return f'Comment by {self.author.username} on {self.blog.title}' 
    
    
class BlogLike(models.Model):
    user  = models.ForeignKey(User,on_delete=models.CASCADE, related_name='liked_blog')
    blog =  models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)  
    

    class Meta:
        unique_together = ['slug','user']


    def __str__(self):
        return f'Comment by {self.user.username} on {self.blog.title}' 
    
@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
    
@receiver(post_save,sender=User)
def save_user_profile(sender,instance,created,**kwargs):
    
        instance.profile.save()
        