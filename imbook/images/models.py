from django.db import models
from django.conf import settings
from django.utils.text import slugify
import requests
from django.core.files.base import ContentFile

class Image(models.Model):
     user = models.ForeignKey(settings.AUTH_USER_MODEL,
     related_name='images_created')
     title = models.CharField(max_length=200)
     slug = models.SlugField(max_length=200,
     blank=True)
     url = models.URLField()
     image = models.ImageField(upload_to='images/%Y/%m/%d')
     description = models.TextField(blank=True)
     created = models.DateField(auto_now_add=True,
     db_index=True)
     users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
     related_name='images_liked',
     blank=True)
    
def save(self, force_insert=False,
        force_update=False,
        commit=True):
     image = super(ImageCreateForm, self).save(commit=False)
     image_url = self.cleaned_data['url']
     image_name = '{}.{}'.format(slugify(image.title),
     image_url.rsplit('.', 1)[1].lower())
     # download image from the given URL
     response = requests.get(image_url)
     image.image.save(image_name,
        ContentFile(response.read()),
        save=False)
     if commit:
        image.save()
     return image


     def __str__(self):
        return self.title