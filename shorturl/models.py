from django.db import models


class MainPage(models.Model):
    services = models.CharField(max_length=200)

    def __str__(self):
        return self.services


class UrlModel(models.Model):
    url = models.CharField(max_length=150)
    slug = models.CharField(max_length=15)

    def __str__(self):
        template = '{0.url} {0.slug}'
        return template.format(self)

