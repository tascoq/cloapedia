from django.db import models
from PIL import Image

from users.models import Profile


class Category(models.Model):
    COLOR_CHOICES = (
        ('pink', 'pink'),
        ('red', 'red'),
        ('aqua', 'aqua'),
        ('green', 'green'),
        ('grey', 'grey'),
        ('yellow', 'yellow'),
        ('custom-blue', 'custom-blue'),
        ('orange', 'orange'),
    )

    title = models.CharField(max_length=255)
    color = models.CharField(choices=COLOR_CHOICES, max_length=12,
                             blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 related_name='posts', blank=True, null=True)
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL,
                               related_name='posts', blank=True, null=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='posts', blank=True, null=True)
    post = models.TextField()
    rating = models.PositiveIntegerField(default=0)
    seen_amount = models.PositiveIntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
