from django.db import models


class Post(models.Model):
    BOARD_CHOICES = (
        ('공지사항', '공지사항'),
        ('스터디/팀플', '스터디/팀플'),
    )
    postid = models.AutoField(primary_key=True)
    userid = models.ForeignKey('user.User', models.DO_NOTHING, db_column='userid', blank=True, null=True)
    courseid = models.ForeignKey('timetable.Course', models.DO_NOTHING, db_column='course_id', blank=True, null=True)
    title = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)
    content = models.TextField()
    post_type = models.CharField(max_length=10, default='공지사항', choices=BOARD_CHOICES)
    is_closed = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'post'


class PostLike(models.Model):
    userid = models.ForeignKey('user.User', models.DO_NOTHING, db_column='userid', primary_key=True)
    postid = models.ForeignKey(Post, models.DO_NOTHING, db_column='postid')

    class Meta:
        managed = False
        db_table = 'post_like'
        unique_together = (('userid', 'postid'),)

