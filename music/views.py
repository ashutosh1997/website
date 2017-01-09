from django.http import HttpResponse
from django.template import loader

# Create your views here.


def index(request):
    template = loader.get_template('music/index.html')
    return HttpResponse(template.render(request))


def semester1(request):
    template = loader.get_template('music/semester1.html')
    return HttpResponse(template.render(request))


def semester2(request):
    template = loader.get_template('music/semester2.html')
    return HttpResponse(template.render(request))


def semester3(request):
    template = loader.get_template('music/semester3.html')
    return HttpResponse(template.render(request))


def semester4(request):
    template = loader.get_template('music/semester4.html')
    return HttpResponse(template.render(request))


def semester5(request):
    template = loader.get_template('music/semester5.html')
    return HttpResponse(template.render(request))


