# Generated by Django 4.0.6 on 2022-07-23 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0005_alter_event_info_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
