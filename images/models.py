from django.conf import settings
from django.db import models
from django.utils.text import slugify


class Image(models.Model):
    """ Модель для хранения изображений """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='images_created')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    url =models.URLField(max_length=2000)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='images_liked', blank=True)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        indexes = [models.Index(fields=['-created'])]
        ordering = ['-created']

    def save(self, *args, **kwargs):
        """ если поле slug не указано пользователем,
         то будет сгенерировано автоматически на основе поля title """
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
