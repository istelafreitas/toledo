from django.db import models


class Produto(models.Model):
    product = models.CharField('Produto',max_length=100)
    price = models.DecimalField('Valor', decimal_places=2, max_digits=8)
    description = models.TextField(blank=True, null=True)
    phone = models.CharField('Contato',max_length=11)
    photo = models.ImageField('Foto',upload_to='classificados')
    begin_date = models.DateTimeField(auto_now_add=True)



    class Meta:
        db_table = 'produto'