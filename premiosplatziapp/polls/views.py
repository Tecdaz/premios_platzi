from django.http import HttpResponse
from django.shortcuts import render

from .models import Question


def index(request):
    # List of Questions from db
    latest_question_list = Question.objects.all()
    context = {
        "latest_question_list": latest_question_list
    }
    return render(request, 'polls/index.html', context=context)


def detail(request, question_id):
    return HttpResponse(f"Estas viendo la pregunta numero {question_id}")


def results(request, question_id):
    return HttpResponse(f'Estas viendo los resultados de la pregunta numero {question_id}')


def vote(request, question_id):
    return HttpResponse(f'Estas votando a la pregunta numero {question_id}')
