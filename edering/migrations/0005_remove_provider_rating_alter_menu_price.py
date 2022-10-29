# Generated by Django 4.0.6 on 2022-10-29 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edering', '0004_alter_rating_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='provider',
            name='rating',
        ),
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.DecimalField(decimal_places=3, help_text='Decimal Digit', max_digits=10, verbose_name='Menu Item price'),
        ),
    ]
