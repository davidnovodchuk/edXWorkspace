from django.shortcuts import render_to_response
from models import *
from django.http import HttpResponse
import json


def index(request):

    auth_user_list = auth_user.objects.all().order_by('id')

    extra_context = {"auth_user": auth_user_list}

    #return HttpResponse("Hello World!")
    return render_to_response("testProject/index.html", extra_context)


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