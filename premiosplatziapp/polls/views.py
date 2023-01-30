from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Question


def index(request):
    # List of Questions from db
    latest_question_list = Question.objects.all()
    context = {
        "latest_question_list": latest_question_list
    }
    return render(request, 'polls/index.html', context=context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id, )
    context = {
        'question': question
    }
    return render(request, 'polls/detail.html', context=context)


def results(request, question_id):
    return HttpResponse(f'Estas viendo los resultados de la pregunta numero {question_id}')


def vote(request, question_id):
    question = Question.objects.get(pk=question_id)
    selected_choice = question.choice_set.get(pk=request.POST["choice"])
    selected_choice.votes += 1
    selected_choice.save()

    return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
