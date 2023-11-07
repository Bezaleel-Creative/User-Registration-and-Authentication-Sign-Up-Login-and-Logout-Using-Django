from django.db import models

# Create your models here.
class Service_Category(models.Model):
    service_name = models.CharField(max_length=50, default="Online")
    def __str__(self):
        return self.service_name
    

class Online_Appointment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    service = models.ForeignKey(Service_Category, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return self.name