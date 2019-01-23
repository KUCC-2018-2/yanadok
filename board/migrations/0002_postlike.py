# Generated by Django 2.1.4 on 2019-01-23 22:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostLike',
            fields=[
                ('userid', models.ForeignKey(db_column='userid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'post_like',
                'managed': False,
            },
        ),
    ]