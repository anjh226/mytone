from django.db import models

# Create your models here.
class PicUpload(models.Model):
   name = models.CharField(max_length=30)
   pic = models.ImageField(upload_to='media/')

   def _unicode_(self):
       return self.name