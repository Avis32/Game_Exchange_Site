# Generated by Django 3.0.2 on 2020-01-20 19:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform_type', models.CharField(max_length=64, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_price', models.FloatField()),
                ('price', models.FloatField()),
                ('when_to_reset', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=256)),
                ('added_date', models.DateField(auto_now=True)),
                ('location', models.TextField(blank=True)),
                ('review', models.TextField(max_length=512)),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games', to='GameExchange.Platform')),
                ('price', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='GameExchange.Price')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]