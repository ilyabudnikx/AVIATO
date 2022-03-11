# Generated by Django 4.0.3 on 2022-03-11 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aviato_dev', '0003_alter_news_options_alter_news_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-time_create', 'title'], 'verbose_name': 'Новости'},
        ),
        migrations.AddField(
            model_name='news',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
