from django.shortcuts import render
from django.http import HttpResponse
from .models import FirstModel


# Create your views here.

def text_views(request):
    return HttpResponse("<h1>Hello world<h1>")


def home_views(request):
    # for any random data to pass on html from view
    dict = {
        "var1": "value1",
        "list1": [1, 2, "three"]
    }

    return render(request, "index.html", dict)


def about_views(request):
    # data to pass from DB to html
    data_by_id1 = FirstModel.objects.get(id=1)
    print(data_by_id1.title)  # just for checking

    data_of_id_1 = {
        "title": data_by_id1.title,  # use them as a var in about html
        "name": data_by_id1.name,  # use like {{ title }} bexoz data_by_id1 already used here
        "date": data_by_id1.date,
    }

    data_by_id2 = FirstModel.objects.get(id=2)
    data_of_id_2 = {
        "object2": data_by_id2,  # use like {{ object2.title }}
    }

    return render(request, 'about.html', data_of_id_1)


def contact_views(request):
    # data to pass from DB to html

    data_by_id2 = FirstModel.objects.get(id=2)
    data_of_id_2 = {
        "object2": data_by_id2,  # use like {{ object2.title }}
    }

    return render(request, 'contact.html', data_of_id_2)
