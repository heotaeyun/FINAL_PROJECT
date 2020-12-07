from django.db import models

# Create your models here.

class Movies(models.Model):
    title   = models.CharField(max_length=45)
    img_url = models.CharField(max_length=1200)
    story   = models.TextField()
    people  = models.CharField(max_length=20)
    rate    = models.DecimalField(max_digits=4, decimal_places=1) #안에 인자값 확인 요망 실제 데이터랑!!
    genre   = models.CharField(max_length=350)

    
