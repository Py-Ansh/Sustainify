# models.py
from django.db import models
from django.contrib.auth.models import User

class Discussion(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Reply(models.Model):
    discussion = models.ForeignKey(Discussion, related_name='replies', on_delete=models.CASCADE)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Reply by {self.created_by} on {self.created_at}'




class CompostingPit(models.Model):
    name = models.CharField(max_length=255)  # Name of the composting pit
    location = models.CharField(max_length=255)  # Address or description of the composting pit
    latitude = models.DecimalField(max_digits=9, decimal_places=6)  # Latitude for the map
    longitude = models.DecimalField(max_digits=9, decimal_places=6)  # Longitude for the map
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="composting_pits")  # User who created the pit

    def __str__(self):
        return self.name
