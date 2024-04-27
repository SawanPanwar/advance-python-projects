# Generated by Django 2.2.5 on 2024-04-26 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marksheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollno', models.IntegerField(max_length=20)),
                ('name', models.CharField(max_length=30)),
                ('physics', models.FloatField(max_length=3)),
                ('chemistry', models.FloatField(max_length=3)),
                ('maths', models.FloatField(max_length=3)),
            ],
            options={
                'db_table': 'SOS_MARKSHEET',
            },
        ),
    ]
