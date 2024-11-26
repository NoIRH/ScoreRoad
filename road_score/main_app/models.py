from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Segment(models.Model):
    start_point = models.CharField(max_length=255)
    end_point = models.CharField(max_length=255)

class AI_segment_mark(models.Model):
    segment = models.ForeignKey(Segment, on_delete = models.CASCADE)
    mark = models.CharField(max_length=255)
    create_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(default=timezone.now)

class User_segment_mark(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    segment = models.ForeignKey(Segment, on_delete = models.CASCADE)
    mark = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)
    create_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(default=timezone.now)
