from django.db import models
import uuid
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator

# Create your models here.


class Screen(models.Model):
    id = models.UUIDField(primary_key=True , default=uuid.uuid4 , editable=False)
    name = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)
    rows = models.IntegerField()
    columns = models.IntegerField()
    total_capacity = models.GeneratedField(
        expression=models.F("rows") * models.F("columns"),
        output_field=models.PositiveIntegerField(),
        db_persist=True,
    )
    
    

