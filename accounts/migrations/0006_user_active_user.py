# Generated by Django 4.0.3 on 2022-04-11 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_user_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='active_user',
            field=models.BooleanField(default=True),
        ),
    ]
