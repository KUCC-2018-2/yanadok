# Generated by Django 2.1.4 on 2019-03-06 20:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment_content', models.TextField()),
                ('upload_time', models.DateTimeField(default=datetime.datetime(2019, 3, 6, 20, 56, 9, 813073))),
            ],
            options={
                'db_table': 'comment',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=20, null=True)),
                ('password', models.CharField(blank=True, max_length=20, null=True)),
                ('content', models.TextField()),
                ('post_type', models.CharField(choices=[('공지사항', '공지사항'), ('스터디/팀플', '스터디/팀플')], default='공지사항', max_length=10)),
                ('is_closed', models.DateTimeField(blank=True, null=True)),
                ('upload_time', models.DateTimeField(default=datetime.datetime(2019, 3, 6, 20, 56, 9, 811072))),
            ],
            options={
                'db_table': 'post',
            },
        ),
        migrations.CreateModel(
            name='PostLike',
            fields=[
                ('post_like_id', models.AutoField(primary_key=True, serialize=False)),
                ('post_id', models.ForeignKey(blank=True, db_column='post_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='board.Post')),
            ],
            options={
                'db_table': 'post_like',
            },
        ),
    ]
