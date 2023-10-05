from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class MenuItem(MPTTModel):
    title = models.CharField(max_length=100, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    url = models.CharField('Link',max_length=200)
    position = models.PositiveIntegerField('Position', default=1)


    class MPTTMeta:
        order_insertion_by = ['position']

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Menu item'
        verbose_name_plural = 'Menu items'
