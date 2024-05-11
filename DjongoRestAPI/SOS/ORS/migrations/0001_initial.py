# Generated by Django 4.1.13 on 2024-05-04 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marksheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollno', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('physics', models.FloatField()),
                ('chemistry', models.FloatField()),
                ('maths', models.FloatField()),
            ],
        ),
    ]
