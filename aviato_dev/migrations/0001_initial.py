# Generated by Django 4.0.3 on 2022-03-09 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=256)),
                ('password', models.CharField(max_length=256)),
                ('time_create_account', models.DateTimeField(auto_now_add=True)),
                ('avatar', models.ImageField(upload_to='photos/%Y/%m/%d/')),
            ],
        ),
    ]
