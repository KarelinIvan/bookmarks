from django import forms

from images.models import Image
from django.core.files.base import ContentFile
from django.utils.text import slugify
import requests


class ImageCreateForm(forms.ModelForm):
    """ Форма для передачи изображений """

    class Meta:
        model = Image
        fields = ['title', 'url', 'description', ]
        widgets = {'url': forms.HiddenInput, }

    def clean_url(self):
        """ Форма валидации расширения изображения """
        url = self.cleaned_data['url']
        valid_extensions = ['.jpg', '.jpeg', '.png', ]
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('Указанный URL-адрес не соответствует допустимым расширениям изображений')
        return url

    def save(self, force_insert=False, force_update=False, commit=True):
        """ Функция для сохранения объекта в базе данных """
        image = super().save(commit=False)
        image_url = self.cleaned_data['url']
        name = slugify(image.title)
        extension = image_url.rsplit('.', 1)[1].lower()
        image_name = f'{name}.{extension}'
        response = requests.get(image_url)
        image.image.save(image_name, ContentFile(response.content), save=False)
        if commit:
            image.save()
        return image
