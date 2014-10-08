from django.shortcuts import render_to_response
from models import *
from django.http import HttpResponse


def index(request):

    student_courseenrollment_list = student_courseenrollment.objects.all()

    extra_context = {"student_courseenrollment": student_courseenrollment_list}

    #return HttpResponse("Hello World!")
    return render_to_response("testProject/index.html", extra_context)


def state(request):

    state = courseware_studentmodule.objects.all()[0]

    return HttpResponse(state.state)