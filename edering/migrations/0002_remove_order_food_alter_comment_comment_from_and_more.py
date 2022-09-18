# Generated by Django 4.0.6 on 2022-09-16 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edering', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='food',
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_comment_from', to='edering.customer', verbose_name='Comment customer'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='rating',
            field=models.FloatField(help_text='4.5', verbose_name='Hotel Rating'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_id', to='edering.customer', verbose_name='Ordered customer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_id', to='edering.hotel', verbose_name='Ordered Hotel'),
        ),
        migrations.AlterField(
            model_name='userscan',
            name='id',
            field=models.CharField(help_text='Required and Unique', max_length=100, primary_key=True, serialize=False, unique=True, verbose_name='UserScan id '),
        ),
    ]
