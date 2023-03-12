# Generated by Django 4.1.7 on 2023-03-12 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0003_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_id', models.IntegerField()),
                ('unit', models.PositiveIntegerField()),
                ('price', models.IntegerField()),
                ('size', models.CharField(max_length=8)),
            ],
        ),
    ]
