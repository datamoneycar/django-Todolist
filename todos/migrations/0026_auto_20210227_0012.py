# Generated by Django 3.1.6 on 2021-02-26 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0025_auto_20210224_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]
