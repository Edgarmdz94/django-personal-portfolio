# Generated by Django 3.0.7 on 2020-07-07 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_login_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='last_login',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='login',
            name='signup_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]