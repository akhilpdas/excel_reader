from django.db import models
import jsonfield

# Create your models here.

class ExcelInfo(models.Model):
    """To save attribute of an entity."""

    file_name = models.CharField(max_length=100)
    data = jsonfield.JSONField(default=dict)
