from django.db import models

# Create your models here.
class Position(models.Model):
    position = models.CharField(max_length=50, default="Online")
    def __str__(self):
        return self.position
class Teamphoto(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    staff_possition = models.ForeignKey(Position, on_delete=models.CASCADE)
    photo = models.ImageField(blank=True, upload_to='imagesz')

    def __str__(self):
        return self.name
