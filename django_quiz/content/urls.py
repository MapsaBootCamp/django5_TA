from django.urls import path
from .views import question_detail, QuestionDetail, QuestionList, \
    answer_question, AnswerCount, CreateQuestion

urlpatterns = [
    path('question-detail/<int:question_id>/',
         question_detail,
         name='question-detail-1'),
    path('class-question-detail/<int:question_id>/',
         QuestionDetail.as_view(),
         name='question-detail'),
    path('class-question-list/', QuestionList.as_view(),
         name='question-list'),
    path('answer_question/<int:question_id>/', answer_question,
         name='answer-question'),
    path('answer_count/<int:question_id>/', AnswerCount.as_view(),
         name='answer-count'),
    path('create-question/', CreateQuestion.as_view(),
         name='create-question')
]