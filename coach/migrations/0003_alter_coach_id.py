# Generated by Django 3.2.18 on 2023-03-23 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coach', '0002_alter_coach_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]