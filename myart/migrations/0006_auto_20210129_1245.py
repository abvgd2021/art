# Generated by Django 3.1.3 on 2021-01-29 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myart', '0005_auto_20210129_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='bio',
            field=models.TextField(default='bio', help_text='Enter a bio', max_length=500),
        ),
    ]
