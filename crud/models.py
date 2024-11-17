from django.db import models

# Create your models here.
class Player(models.Model):
    """
    Player Model for CRUD operations
    """
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    team = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', default='images/default.jpg')

    def __str__(self):
        return self.name