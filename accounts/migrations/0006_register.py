# Generated by Django 4.0.5 on 2022-07-12 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_user_managers_user_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('username', models.CharField(max_length=300)),
                ('password', models.CharField(max_length=300)),
            ],
        ),
    ]
