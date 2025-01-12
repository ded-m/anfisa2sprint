# Generated by Django 3.2.16 on 2023-05-10 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0002_auto_20230510_1531'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категории', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='icecream',
            options={'verbose_name': 'Мороженое', 'verbose_name_plural': 'Мороженое'},
        ),
        migrations.AlterModelOptions(
            name='topping',
            options={'verbose_name': 'Топпинги', 'verbose_name_plural': 'Топпинги'},
        ),
        migrations.AlterModelOptions(
            name='wrapper',
            options={'verbose_name': 'Обёртки', 'verbose_name_plural': 'Обёртки'},
        ),
        migrations.AlterField(
            model_name='icecream',
            name='toppings',
            field=models.ManyToManyField(to='ice_cream.Topping', verbose_name='Топпинги'),
        ),
    ]
