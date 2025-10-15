from django.db import models

# Create your models here.
class Car(models.Model):    
    model = models.CharField(max_length=100)
    car_image = models.ImageField(max_length=100, upload_to='images/', blank=True)
    price_per_d = models.DecimalField(max_digits=6,decimal_places=2)
    is_available = models.BooleanField(default=True)
    

    def __str__(self):
        return f"{self.model} (${self.price_per_d},day)"
    

class Rental(models.Model):
    username = models.CharField(max_length=100)
    car = models.ForeignKey(Car,on_delete=models.CASCADE)
    days  = models.PositiveBigIntegerField()
    total_cost = models.DecimalField(max_digits=8,decimal_places=2)
    rented_at =models.DateTimeField(auto_now_add=True)
    returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username} - {self.car.model}"
