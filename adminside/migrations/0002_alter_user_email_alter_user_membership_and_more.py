# Generated by Django 5.1.2 on 2024-10-13 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminside', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='membership',
            field=models.CharField(choices=[('free', 'Free'), ('premium', 'Premium'), ('vip', 'VIP')], default='free'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('agency', 'Agency'), ('user', 'User')], default='user'),
        ),
    ]
