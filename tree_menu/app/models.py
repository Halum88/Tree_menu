from django.db import models
from django.urls import reverse

class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    content = models.TextField(verbose_name='Content')

    def get_absolute_url(self):
        return reverse('page_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
