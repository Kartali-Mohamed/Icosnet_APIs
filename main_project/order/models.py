from django.db import models
import uuid
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# Create your models here.
class OrderStatus(models.TextChoices):
    PENDING = 'Pending' 
    PROCESSING = 'Processing' 
    SHIPPED = 'Shipped'
    DELIVERED = 'Delivered'
    CANCELLED = 'Cancelled'

class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, unique=True, blank=False)
    description = models.TextField(max_length=1000,default="",blank=False)
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=False)
    status = models.CharField(max_length=60, choices=OrderStatus.choices, default=OrderStatus.PENDING)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    createAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
    
    def clean(self):
    # Validate that the title is not empty
        if not self.title.strip():
            raise ValidationError({'title': 'Title cannot be empty.'})
        
    class Meta:
        unique_together = ('title',)