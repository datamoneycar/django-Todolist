# Generated by Django 3.1.6 on 2021-02-17 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0010_remove_todo_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='Catrgory',
            field=models.CharField(default='undifined category', max_length=50),
            preserve_default=False,
        ),
    ]
