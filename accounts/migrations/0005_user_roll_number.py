# Generated by Django 4.0.3 on 2022-03-31 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='roll_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]