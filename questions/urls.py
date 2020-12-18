from django.urls import path

from . import views

urlpatterns = [
    path('new-question/<int:pk>/', views.NewQuestionView.as_view(), name='new_question'),
    path('new-reply/<int:pk>/', views.NewReplyView.as_view(), name='new_reply'),
]
