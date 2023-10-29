from django.shortcuts import render

#my imports
from apps.index.models import Settings
from apps.jobs.models import Jobs
from django.shortcuts import render


def index(request):
    return render(request, "base/index.html", locals())

def header(request, id):
    # setting = Settings.objects.latest('id')
    return render(request, 'index/header.html', locals())
# CV

def homepage(request):
    # setting = Settings.objects.latest('id')
    return render(request, "index/homepage.html", locals())

