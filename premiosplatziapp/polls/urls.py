from django.urls import path

from . import views

urlpatterns = [
    path("results/<int:question_id>/", views.results, name='results'),
    path("vote/<int:question_id>/", views.vote, name='vote'),
    path("detail/<int:question_id>/", views.detail, name='detail')
]
