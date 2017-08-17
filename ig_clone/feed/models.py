from django.db import models

# Create your models here.
class FileIt(models.Model):
    description = models.CharField(max_length=255, blank=True)
    file_it = models.FileField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
