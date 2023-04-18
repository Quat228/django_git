from django.http import HttpResponse


def index():
    return HttpResponse('index')


def about():
    return HttpResponse('about')
