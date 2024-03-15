from django.urls import path

from question_bank_api.views.all_questions import AllQuestions
from question_bank_api.views.create_question import CreateQuestion

urlpatterns = [
    path("all_questions", AllQuestions.as_view()),
    path("add_question", CreateQuestion.as_view()),
]