from django.db import models
import datetime
from django.contrib.auth.models import User
from django_cryptography.fields import encrypt

# Create your models here.
class memory(models.Model):
    
    content=encrypt(models.TextField())
    title=models.TextField(default="Good Day!")
    #date=models.DateField(("Date"),default=datetime.date.today)
    date=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE, ) 

    def __str__(self):
        return 'Entry #{}'.format(self.id)