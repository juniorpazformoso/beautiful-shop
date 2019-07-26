from django.db import models
from django.utils.translation import ugettext_lazy as _

class Country(models.Model):
    """
    A country.
    """
    name = models.CharField(_("Name"), max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")
        ordering = ('name',)


class City(models.Model):
    """
    A city.
    """
    name = models.CharField(_("Name"), max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("City")
        verbose_name_plural = _("Cities")
        ordering = ('name',)


class Cap(models.Model):
    '''CAP for cities'''
    cap = models.CharField(max_length=50)

    def __str__(self):
        return self.cap

    class Meta:
        verbose_name = _("CAP")
        ordering = ('cap',)


