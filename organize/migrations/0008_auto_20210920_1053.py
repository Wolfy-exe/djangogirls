# Generated by Django 3.2.7 on 2021-09-20 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organize', '0007_auto_20210906_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coorganizer',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='eventapplication',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
