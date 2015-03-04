from django.shortcuts import render_to_response
from models import *
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
import re
import datetime
from datetime import timedelta

def index(request):

    auth_user_list = auth_user.objects.all().order_by('id')

    extra_context = {"auth_user": auth_user_list}

    #return HttpResponse("Hello World!")
    return render_to_response("testProject/index.html", extra_context)

"""
#
# old code
#

def state(request):

    studentId = 6

    # in order to get records of all students
    # studentModule = courseware_studentmodule.objects.all()

    # in order to get records of a student with particular student_id
    # and the module_type is 'Problem'
    studentModule = courseware_studentmodule.objects.filter(
            student_id = studentId
        ).filter(
            module_type = 'Problem'
        )

    problems = []

    for row in studentModule:

        state = json.loads(row.state)
        attempts = 0
        #search in the state JSON array if there were attempts performed on
        #the current problem
        for key, value in state.iteritems ():
            if key == "attempts":

                attempts = value
                # checking if the student attempted to solve the problem
                if attempts > 0:
                    problem = {}
                    # problem is an associative array that stores values and keys (instead of indexes)
                    problem["problem_code"] = row.module_id
                    problem["attempts"] = attempts
                    problem["grade"] = int ( row.grade / row.max_grade * 100 )
                    problem["time_took"] = row.modified - row.created

                    problems.append(problem)

    extra_context = { "student_id": studentId,
                      "student_state": problems}

    return render_to_response("testProject/state.html", extra_context)
"""
def courses(request):

    # print "-----------------"

    studentModule = courseware_studentmodule.objects.filter(
            module_type = 'Problem'
        )

    courses = []

    for row in studentModule:

        course_id = row.course_id

        if not any(course_id in s for s in courses):

            courses.append(course_id)

    extra_context = { "courses": courses }

    return render_to_response("testProject/courses.html", extra_context)


def specifiedCourse(request, course_id):

    if request.method == 'POST': # If the form has been submitted...

        student_ids = request.POST.getlist('student_ids')
        problem_ids = request.POST.getlist('problem_ids')

        #hidden fields
        course_students = request.POST.getlist('students')
        course_id = request.POST.get('course_id')

        # getting times of all course components (courses, chapters, sequentials, problems)
        timesModule = courseware_studentmodule.objects.filter(
                    course_id = course_id
                )

        times = []
        for row in timesModule:
            timeRow = {}
            timeRow["module_type"] = row.module_type
            timeRow["module_id"] = row.module_id
            timeRow["created"] = row.created

            times.append(timeRow)

        times.sort(key=lambda x: x["created"])
        print times

        # in case student_ids array is empty, using all students enrolled in course
        if not student_ids:
            student_ids = re.findall('\d+', course_students[0])

        # student_states stores student's interaction with different problems
        student_states = []

        for studentId in student_ids:

            # in order to get records of all students
            # studentModule = courseware_studentmodule.objects.all()

            # in order to get records of a student with particular student_id
            # and the module_type is 'Problem'
            studentModule = courseware_studentmodule.objects.filter(
                    course_id = course_id
                ).filter(
                    module_type = 'Problem'
                ).filter(
                    student_id = studentId
                )

            problems = []
            attemptsArr = []
            gradeArr = []
            timeTookArr = []

            for row in studentModule:

                # check if current problem_id is in passed problem_ids array
                if any(row.module_id in s for s in enumerate(problem_ids)) or not problem_ids:

                    state = json.loads(row.state)
                    attempts = 0
                    #search in the state JSON array if there were attempts performed on
                    #the current problem
                    for key, value in state.iteritems ():
                        if key == "attempts":

                            attempts = value
                            # checking if the student attempted to solve the problem
                            if attempts > 0:
                                problem = {}

                                # problem is an associative array that stores values and keys (instead of indexes)
                                problem["problem_code"] = row.module_id.split("/problem/", 1)[1]
                                problem["attempts"] = attempts
                                attemptsArr.append(attempts)
                                problem["grade"] = int ( row.grade / row.max_grade * 100 )
                                gradeArr.append(problem["grade"])
                                problem["time_took"] = row.modified - row.created
                                timeTookArr.append(problem["time_took"])

                                problems.append(problem)

            student_state = {}
            student_state["student_id"] = studentId
            student_state["problems"] = problems
            # claculating averages of attempts, grades, and time took
            student_state["avg_attempts"] = float(sum(attemptsArr)) / float(len(attemptsArr))
            student_state["avg_grade"] = sum(gradeArr) / len(gradeArr)
            student_state["avg_time_took"] = sum(timeTookArr, datetime.timedelta(0)) / len(timeTookArr)
            # adding all problems current student tackled
            student_states.append(student_state)

        extra_context = { "student_ids": student_ids,
                          "student_states": student_states}

        return render_to_response("testProject/result.html", extra_context)

    else:

        #course_id = "cdot/1/2015_01"

        studentModule = courseware_studentmodule.objects.filter(
                module_type = 'Problem'
            ).filter(
                course_id = course_id
            )

        students = []
        added_problem_ids = []
        problems = []

        for row in studentModule:

            # checking is a gradable problem
            if row.max_grade >= 0:

                # students enrolled on the course
                student_id = row.student_id

                # checking that there are no repetitions
                if not any(student_id in s for s in enumerate(students)):

                    students.append(student_id)

                if not any(row.module_id in s for s in enumerate(added_problem_ids)):
                    added_problem_ids.append(row.module_id)
                    # information about gradable problems in the course
                    problem = {}
                    problem["problem_id"] = row.module_id
                    problem["max_grade"] = row.max_grade

                    problems.append(problem)

        extra_context = { "course_id": course_id,
                          "students": students,
                          "problems": problems}

        return render_to_response("testProject/courses/view_course.html", extra_context,
                               context_instance=RequestContext(request))