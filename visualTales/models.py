#from os.path import dirname, realpath
from django.db import models
# Create your models here.

#absolutePath = dirname(realpath(__file__)) + '/' # models.ImageField must take a relative path, not an absolute path # Delete

class Image(models.Model):
  phrase = models.CharField(max_length = 200)
  ai_image = models.ImageField(upload_to='visualTales/images')#absolutePath + 'images')
  def __str__(self):
    return str(self.phrase)
