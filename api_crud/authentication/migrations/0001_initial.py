# Generated by Django 3.2.9 on 2021-11-07 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, verbose_name='Username')),
                ('password', models.CharField(max_length=150, verbose_name='Passsword')),
            ],
        ),
    ]