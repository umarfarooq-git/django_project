from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class test(models.Model):
    test_name=models.CharField(max_length=40)
    test_details=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    test_marks=models.IntegerField()



    def __str__(self):
        return self.test_name

    def get_absolute_url(self):
        return reverse('about-test')



# Create your models here.
