# Generated by Django 4.0.6 on 2022-07-25 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0007_alter_images_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to='static/event_images'),
        ),
    ]
