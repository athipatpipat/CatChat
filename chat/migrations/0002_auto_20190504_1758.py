# Generated by Django 2.1.5 on 2019-05-04 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='room_number',
            field=models.IntegerField(),
        ),
    ]
