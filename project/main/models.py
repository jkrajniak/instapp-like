from django.db import models
import jsonfield

class Image(models.Model):
    """Model to store data related to the uploaded image."""
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='raw_pic/',
                              default='raw_pic/no-image.png',
                              blank=True,
                              null=True)
    visual_attrs = jsonfield.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
