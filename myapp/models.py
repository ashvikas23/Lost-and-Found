from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    CATEGORY_CHOICES=[
        ('Lost','Lost'),
        ('Found','Found'),
    ]

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    category=models.CharField(max_length=10,choices=CATEGORY_CHOICES)
    location=models.CharField(max_length=100)
    date=models.DateField()
    description=models.TextField()
    image=models.ImageField(upload_to='items/', blank=True, null=True)

    def __str__(self):
        return self.title

