# Generated by Django 4.0.6 on 2022-09-11 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0009_alter_images_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='image',
        ),
        migrations.AddField(
            model_name='images',
            name='field_name',
            field=models.ImageField(default='exit', upload_to=None),
            preserve_default=False,
        ),
    ]