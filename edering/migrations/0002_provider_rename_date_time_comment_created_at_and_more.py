# Generated by Django 4.0.6 on 2022-10-27 03:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('edering', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.CharField(help_text='Required and Unique', max_length=255, primary_key=True, serialize=False, unique=True, verbose_name='Provider id ')),
                ('name', models.CharField(help_text=' Required ', max_length=255, verbose_name='Provider name')),
                ('location', models.CharField(help_text=' Required , (lat, lng) ', max_length=100, verbose_name='Provider location')),
                ('image_id', models.URLField(help_text='https://my_image.png', max_length=500, verbose_name='Provider Profile Image Url')),
                ('known_for', models.CharField(help_text=' Not Required', max_length=100, verbose_name='famous food ')),
                ('rating', models.FloatField(help_text='4.5', verbose_name='Provider Rating')),
                ('open_time', models.CharField(help_text='10:00 AM', max_length=100, verbose_name='Provider open time ')),
                ('close_time', models.CharField(help_text='10:00 PM', max_length=100, verbose_name='Provider close time ')),
                ('created_at', models.CharField(help_text='Timesamp take default timestamp', max_length=255, verbose_name='Account created timestamp')),
            ],
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='date_time',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='foodcategory',
            old_name='image_uri_id',
            new_name='image_id',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='auth_id',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='category',
        ),
        migrations.RemoveField(
            model_name='order',
            name='delivered_status',
        ),
        migrations.RemoveField(
            model_name='order',
            name='food',
        ),
        migrations.RemoveField(
            model_name='userscan',
            name='user_id',
        ),
        migrations.AddField(
            model_name='menu',
            name='foodCategory',
            field=models.ForeignKey(default='mom', on_delete=django.db.models.deletion.CASCADE, related_name='menus', to='edering.foodcategory', verbose_name='Food Category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='food_count',
            field=models.IntegerField(default=23, help_text='Not Required', verbose_name='food count '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='food_name',
            field=models.CharField(default='fsd', help_text='Not Required', max_length=255, verbose_name='food name '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='order_cost',
            field=models.DecimalField(decimal_places=3, default=5235, help_text='Total cost of order', max_digits=10, verbose_name='Order cost'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.CharField(default='sdsdf', help_text='Canceled, approved ... ', max_length=255, verbose_name='Order Status'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userscan',
            name='customer_id',
            field=models.ForeignKey(default='sfdsdf', on_delete=django.db.models.deletion.CASCADE, related_name='user_scan', to='edering.customer', verbose_name='Scanned customer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_comment_from', to='edering.customer', verbose_name='Comment customer'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.CharField(help_text='Required and Unique', max_length=255, primary_key=True, serialize=False, unique=True, verbose_name='Comment Id'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.CharField(help_text='Required and Unique', max_length=255, primary_key=True, serialize=False, unique=True, verbose_name='Customer id'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_order', to='edering.customer', verbose_name='Order from'),
        ),
        migrations.AlterField(
            model_name='userscan',
            name='id',
            field=models.AutoField(help_text='Auto increment int', primary_key=True, serialize=False, unique=True, verbose_name='UserScan id '),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(help_text='auto increment, int id', primary_key=True, serialize=False, unique=True, verbose_name='rating id')),
                ('rating', models.DecimalField(decimal_places=3, help_text='decimal valued rating', max_digits=10, verbose_name='rating_value')),
                ('created_at', models.CharField(help_text='time stamp value', max_length=255, verbose_name='date created_at')),
                ('from_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating_from', to='edering.customer', verbose_name='Customer')),
                ('to_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating_to', to='edering.provider', verbose_name='Provider')),
            ],
        ),
        migrations.AddField(
            model_name='foodcategory',
            name='provider',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='food_categories', to='edering.provider', verbose_name='provider'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_comment_to', to='edering.provider', verbose_name='Comment Hotel'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provider_order', to='edering.provider', verbose_name='Order to'),
        ),
        migrations.DeleteModel(
            name='Hotel',
        ),
    ]
