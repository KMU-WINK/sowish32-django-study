# Generated by Django 3.0.8 on 2020-08-03 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myCareerApp', '0002_auto_20200803_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='career',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='github_url',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='kakaoId',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='tech',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='projectboard',
            name='project_img',
            field=models.TextField(null=True),
        ),
    ]