from django.db import models
from django.utils import timezone


class Post(models.Model):
    BOARD_CHOICES = (
        ('공지사항', '공지사항'),
        ('스터디/팀플', '스터디/팀플'),
    )
    post_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('user.User', models.DO_NOTHING, db_column='user_id', blank=True, null=True)
    course_id = models.ForeignKey('timetable.Course', models.DO_NOTHING, db_column='course_id', blank=True, null=True)
    title = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)
    content = models.TextField()
    post_type = models.CharField(max_length=10, default='공지사항', choices=BOARD_CHOICES)
    is_closed = models.DateTimeField(blank=True, null=True)
    upload_time = models.DateTimeField(default=timezone.now())

    class Meta:
        managed = False
        db_table = 'post'


class PostLike(models.Model):
    user_id = models.ForeignKey('user.User', models.DO_NOTHING, db_column='user_id', primary_key=True)
    post_id = models.ForeignKey(Post, models.DO_NOTHING, db_column='post_id')

    class Meta:
        managed = False
        db_table = 'post_like'
        unique_together = (('user_id', 'post_id'),)


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    post_id = models.ForeignKey('board.Post', models.DO_NOTHING, db_column='post_id', blank=True, null=True)
    user_id = models.ForeignKey('user.User', models.DO_NOTHING, db_column='user_id', blank=True, null=True)
    comment_content = models.TextField()
    upload_time = models.DateTimeField(default=timezone.now())

    class Meta:
        managed = True
        db_table = 'comment'
