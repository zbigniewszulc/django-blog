# Generated by Django 4.2.13 on 2024-06-27 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='xcerpt',
            field=models.TextField(blank=True),
        ),
    ]
