import os
import re

import openpyxl
from django.core.management import BaseCommand
from django.db import transaction

from course.models import Course, CourseTime, CourseSpaceTime


class Command(BaseCommand):
    help = ''

    def add_arguments(self, parser):
        pass

    @transaction.atomic
    def handle(self, *args, **options):
        course_id = 1
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
        workbook = openpyxl.load_workbook(BASE_DIR + '/course_data.xlsx')
        sheet = workbook.get_sheet_by_name("Sheet1")
        for row in sheet:
            if row[0].row == 1:
                continue

            course_time_spaces = self.__get_course_times(row[8].value)

            course = Course(
                            course_id=course_id,
                            course_no=row[0].value,
                            semester=row[1].value,
                            university=row[2].value,
                            campus=row[3].value,
                            classification=row[4].value,
                            course_name=row[5].value,
                            professor=row[6].value,
                            credit=row[7].value
            )
            course.save()
            course_id += 1
            for course_time_space in course_time_spaces:
                course_time_space.course = course
                course_time_space.save()


    def __get_course_times(self, course_time_str):
        try:
            if course_time_str:
                time_spaces = course_time_str.split(' / ')
                course_time_spaces = []
                order_regex = re.compile('([0-9])')
                for time_space in time_spaces:
                    splited = time_space.split(' ')
                    time = splited[0]
                    space = ' '.join(splited[1:])
                    day = time[:1]
                    for choices in CourseTime.DAY_CHOICES:
                        if choices[1] == day:
                            day = choices[0]
                            break
                    orders = order_regex.findall(time)
                    order_start = int(orders[0])
                    order_end = int(orders[-1]) + 1
                    orders = [i for i in range(order_start, order_end)]
                    for order in orders:
                        course_time = CourseTime.objects.filter(order=order, course_day=day).get()
                        course_time_spaces.append(CourseSpaceTime(course_time=course_time, classroom=space))
                return course_time_spaces

            return []
        except:
            return []
