# Generated by Django 4.0.6 on 2022-10-22 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0013_alter_images_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/event_images'),
        ),
    ]
