from django.db import models

class student_courseenrollment(models.Model):
    id = models.IntegerField(null=True)
    user_id = models.IntegerField(null=True)
    course_id = models.CharField(max_length=255, null=True)
    created = models.DateTimeField(null=True)
    is_active = models.SmallIntegerField(max_length=1, null=True)
    mode = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'student_courseenrollment'


class courseware_studentmodule(models.Model):
    state = models.TextField(null=True)

    class Meta:
        db_table = 'courseware_studentmodule'