from django.http import HttpResponse


def Index():
    return HttpResponse('index')


def about():
    return HttpResponse('about')
