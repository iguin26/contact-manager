from django.db import models
from django.utils import timezone

# Create your models here.

# id (primary key)
# first_name (string), last_name (string), phone (string)
# email (email), created_date (date), description (text)

# category (foreign key), show (boolean), owner (foreign key)
# picture (imagem)

class Contact(models.Model):
    first_name = models.CharField(max_length=51)
    last_name = models.CharField(max_length=51, blank=True)
    phone = models.CharField(max_length=51)
    email = models.EmailField(max_length=255, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m')

    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"