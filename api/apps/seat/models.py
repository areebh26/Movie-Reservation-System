from django.db import models
import uuid
# Create your models here.

class Seat(models.Model):
    id = models.UUIDField(primary_key=True , default=uuid.uuid4 , editable=False)
    seat_number = models.CharField(max_length=10)
    row = models.IntegerField()
    column = models.IntegerField()
    screen = models.ForeignKey('screen.Screen' , on_delete=models.CASCADE)
    
    
