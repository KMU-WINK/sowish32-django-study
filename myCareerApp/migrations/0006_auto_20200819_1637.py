# Generated by Django 3.0.8 on 2020-08-19 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myCareerApp', '0005_auto_20200812_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='', upload_to='static/img/profile', verbose_name='IMAGE'),
        ),
        migrations.AlterField(
            model_name='projectboard',
            name='project_img',
            field=models.ImageField(default='', upload_to='static/img/project', verbose_name='PROJECT IMAGE'),
        ),
    ]