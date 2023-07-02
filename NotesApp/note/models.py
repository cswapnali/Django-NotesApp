from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    CATEGORY_CHOICES = (
        ('text', 'Text'),
        ('audio', 'Audio'),
        ('video', 'Video'),
    )

    title = models.CharField(max_length=100)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    content = models.FileField(upload_to='uploads/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shared_with = models.ManyToManyField(User, related_name='shared_notes', blank=True)

    def __str__(self):
        return self.title