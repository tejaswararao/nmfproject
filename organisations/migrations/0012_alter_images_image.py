# Generated by Django 4.0.6 on 2022-10-21 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0011_remove_images_field_name_images_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/%y'),
        ),
    ]
