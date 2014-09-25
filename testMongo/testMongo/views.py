from django.shortcuts import render_to_response
from models import School
from django.http import HttpResponse


def index(request):

    schools_list = School.objects.all()

    extra_context = {"schools_list": schools_list}

    return render_to_response("testMongo/index.html", extra_context)

    """
    # saving document to School collection
  school = School(name = 'University of Toronto', address = 'Toronto')
  school.save()

  return HttpResponse("<h1>Saved!</h1>")
    """