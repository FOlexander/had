from django.db import models

# Create your models here.
class Plot(models.Model):
    title = models.CharField('Название',max_length=20)
    plot = models.ImageField('Plot', upload_to='media/',null=True)

