# Generated by Django 4.0 on 2022-07-17 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='EventYear',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='events',
            name='EventDate',
            field=models.DateField(),
        ),
    ]
