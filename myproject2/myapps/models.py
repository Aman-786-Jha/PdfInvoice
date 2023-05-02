from django.db import models

# Create your models here.

class Form(models.Model):
    id = models.PositiveIntegerField(primary_key=True,null=False,blank=False)
    seller_name = models.CharField(max_length = 200)
    seller_phone = models.PositiveIntegerField(max_length= 10)
    seller_email = models.EmailField()
    buyer_name = models.CharField(max_length=200)
    buyer_email = models.EmailField(null=False)

    
