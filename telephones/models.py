from django.db import models

# Create your models here.
class Telephones(models.Model):
    name = models.CharField('Ник игрока', max_length=50)
    tel_namber = models.CharField('Номер телефона', max_length=50)
    who_insures_name = models.CharField('Кто страхует(Ник)', max_length=50)
    who_insures_tel_namber =models.CharField('Кто страхует (Номер)', max_length=50)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'
