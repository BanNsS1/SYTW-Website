from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date

class Image(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(blank=False, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    description = models.CharField(max_length=500, default="Just an image")

class Rate(models.Model):
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3,
        choices=RATING_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='rates')
    date = models.DateField(default=date.today)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=500)
    date = models.DateField(default=date.today)
