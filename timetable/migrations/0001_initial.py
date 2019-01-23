# Generated by Django 2.1.4 on 2019-01-23 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.IntegerField(primary_key=True, serialize=False)),
                ('course_no', models.CharField(max_length=20)),
                ('semester', models.CharField(max_length=20)),
                ('university', models.CharField(max_length=20)),
                ('campus', models.CharField(max_length=20)),
                ('classification', models.CharField(max_length=20)),
                ('course_name', models.CharField(max_length=20)),
                ('professor', models.CharField(blank=True, max_length=20, null=True)),
                ('credit', models.IntegerField(blank=True, null=True)),
                ('date_classroom', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'course',
                'managed': False,
            },
        ),
    ]