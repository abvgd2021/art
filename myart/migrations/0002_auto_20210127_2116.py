# Generated by Django 3.1.3 on 2021-01-27 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='bio',
            field=models.CharField(default='default', help_text='Enter a bio', max_length=100),
        ),
        migrations.AddField(
            model_name='artist',
            name='birthplace',
            field=models.CharField(default='default', help_text='Enter a birthplace', max_length=20),
        ),
        migrations.AddField(
            model_name='artist',
            name='edu',
            field=models.CharField(default='default', help_text='Enter a edu', max_length=100),
        ),
    ]