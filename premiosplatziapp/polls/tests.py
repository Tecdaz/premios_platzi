from django.test import TestCase
from django.urls import reverse

from .models import Question, Choice


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """If no question exists, an message is displayed"""
        question = Question.objects.create(question_text="Some text")
        question.save()
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])


class QuestionVoteViewTests(TestCase):

    def test_question_with_choices(self):
        question = Question.objects.create(question_text="Some text")
        choice = Choice.objects.create(question=question, choice_text="some text")
        choice.save()
        question.save()
        choices = question.choice_set.all()
        self.assertNotEqual(len(choices), 0)
