# Generated by Django 3.0 on 2019-12-24 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0004_auto_20191224_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtomodel',
            name='category',
            field=models.ManyToManyField(to='produtos.CategoriaModel', verbose_name='categorias'),
        ),
    ]
