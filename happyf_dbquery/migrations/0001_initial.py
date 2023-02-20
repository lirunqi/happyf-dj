# Generated by Django 4.1 on 2023-02-12 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BeforeMatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.CharField(max_length=200)),
                ('matchid', models.CharField(max_length=200)),
                ('series', models.CharField(max_length=200)),
                ('compid', models.CharField(max_length=200)),
                ('home_odd', models.CharField(max_length=200)),
                ('guest_odd', models.CharField(max_length=200)),
                ('odd_term', models.CharField(max_length=200)),
            ],
        ),
    ]