from django.db import models
from django.forms import model_to_dict


class Course(models.Model):
    course_id = models.IntegerField(primary_key=True)
    course_no = models.CharField(max_length=20)
    semester = models.CharField(max_length=20)
    university = models.CharField(max_length=20)
    campus = models.CharField(max_length=20)
    classification = models.CharField(max_length=20)
    course_name = models.CharField(max_length=200)
    professor = models.CharField(max_length=200, blank=True, null=True)
    credit = models.IntegerField(blank=True, null=True)
    course_times = models.ManyToManyField('CourseTime', through='CourseSpaceTime')

    def is_overlapped(self, course):
        target = course.course_times.all()
        for time in self.course_times.all():
            if time in target:
                return True
        return False

    def to_dict(self):
        result = model_to_dict(self)
        course_times = []
        date_classrooms = []
        for time in result['course_times']:
            course_times.append(model_to_dict(time))
            try:
                date_classrooms.append({'day': time.get_course_day_display(),
                                        'order': time.order,
                                        'classroom': time.coursespacetime_set.get(course=self).classroom})
            except:
                pass
        result['course_times'] = course_times
        result['date_classroom'] = self.__generate_date_classroom_str(date_classrooms)
        return result

    def __generate_date_classroom_str(self, date_classrooms):
        result = []
        classroom_of_day = {date_classroom['day']: date_classroom['classroom'] for date_classroom in date_classrooms}
        orders_grouped_by_day = {}
        for date_classroom in date_classrooms:
            orders_grouped_by_day.setdefault(date_classroom['day'],
                                             [date_classroom['order']]).append(date_classroom['order'])

        for day, orders in orders_grouped_by_day.items():
            min_order = min(orders)
            max_order = max(orders)
            order_str = "{}-{}".format(min_order, max_order) if min_order != max_order else "{}".format(min_order)
            result.append('{}({}) {}'.format(day, order_str, classroom_of_day[day]))

        return ' / '.join(result)

    class Meta:
        db_table = 'course'
        unique_together = (('course_id', 'course_no', 'semester', 'university', 'campus'),)


class CourseTime(models.Model):
    DAY_CHOICES = (
        ('MON', '월'),
        ('TUE', '화'),
        ('WED', '수'),
        ('THU', '목'),
        ('FRI', '금'),
        ('SAT', '토'),
        ('SUN', '일'),
    )
    order = models.IntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    course_day = models.CharField(
        max_length=3,
        choices=DAY_CHOICES,
        default='MON',
    )

    def __eq__(self, other):
        return self.order == other.order

    class Meta:
        db_table = 'course_time'


class CourseSpaceTime(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    course_time = models.ForeignKey('CourseTime', on_delete=models.CASCADE)
    classroom = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = 'course_space_time'
