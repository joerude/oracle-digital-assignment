# Generated by Django 4.0.6 on 2022-07-31 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class_management', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='classroom',
        ),
        migrations.AddField(
            model_name='student',
            name='class_name',
            field=models.CharField(default=12, max_length=100),
            preserve_default=False,
        ),
    ]