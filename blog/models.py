from django.db import models

class Post(models.Model):
    #ost = models.ForeignKey('Kategorii', on_delete=models.CASCADE, blank=True,
                           # null=True, verbose_name='Категория')
    name = models.TextField(verbose_name="от куда")
    nam = models.TextField(verbose_name="куда")
    na = models.TextField(verbose_name="сколько дней")
    data = models.DateTimeField(verbose_name="дата ")
    namber = models.CharField(max_length=1, verbose_name=  'в Росиии(1), ближнее заруюежье(2), за границей(3)')


    def __str__(self):
        return f'{self.name}'


class Bilettts (models.Model):
    kategoria = models.TextField(verbose_name='жд, самолет, автобус')
    na = models.TextField(verbose_name='kuda')
    nam = models.TextField(verbose_name='otkuda')
    name = models.DateTimeField()

    def __str__(self):
        return f'{self.na}'
