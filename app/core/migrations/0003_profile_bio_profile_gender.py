# Generated by Django 4.0.7 on 2022-10-04 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('MALE', '男生'), ('FEMALE', '女生'), ('OTHER', '其他')], default='其他', max_length=6),
        ),
    ]