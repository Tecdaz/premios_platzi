from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from .models import Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.all()


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultView(DetailView):
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = Question.objects.get(pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except KeyError:
        context = {
            "question": question,
            "error_message": "No selecciono ningun mensage"
        }
        return render(request, 'polls/detail.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()

    return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
