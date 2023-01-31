from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    fields = ["question_text"]
    inlines = [ChoiceInline]
    list_display = ("question_text", "pub_date")
    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)
