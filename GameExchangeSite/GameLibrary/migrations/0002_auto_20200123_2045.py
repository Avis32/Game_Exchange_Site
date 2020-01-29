# Generated by Django 3.0.2 on 2020-01-23 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GameLibrary', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price',
            name='when_to_reset',
        ),
        migrations.AlterField(
            model_name='game',
            name='price',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='game', to='GameLibrary.Price'),
        ),
    ]
