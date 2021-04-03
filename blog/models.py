from enum import auto
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):

    name = models.CharField(max_length = 100)
    content = models.TextField()
    # date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=10, default="Mumbai")
    address = models.TextField(default="Maharashtra")
    area =models.CharField(max_length=10, default="Andheri")
    covid_cap=models.IntegerField(default=0)
    norm_cap = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})

class BedRequest(models.Model):
    aadhar_number = models.IntegerField(max_length = 16)
    phone_number = models.IntegerField(max_length = 10)
    email = models.EmailField(default='jmak0015@gmail.com')
    name = models.CharField(max_length =100)
    address = models.CharField(max_length=100)
    # proof= models.ImageField(default = 'default.jpg', upload_to='proof_pics')
    city= models.CharField(max_length = 16)
    pin_code= models.IntegerField(max_length=6)
    gender= models.CharField(max_length = 16)
    age= models.IntegerField(default = 1)
    co_mobidity = models.CharField(max_length = 16)
    ambulance_required = models.CharField(max_length = 16)
    scheme = models.CharField(max_length = 16)
    # preferance = models.CharField(max_length = 16)
    health_centre = models.CharField(max_length = 16,default='KEM')
    tested = models.CharField(max_length = 16)
    symptoms = models.CharField(max_length = 16)

    def __str__(self):
        return self.name