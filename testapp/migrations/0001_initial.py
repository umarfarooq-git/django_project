# Generated by Django 3.2.5 on 2021-08-21 23:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=40)),
                ('test_details', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('test_marks', models.IntegerField()),
            ],
        ),
    ]
