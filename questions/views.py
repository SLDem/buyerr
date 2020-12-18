from django.shortcuts import render, redirect

from django.views.generic import DetailView, TemplateView, FormView, UpdateView
from django.views import View

from .forms import QuestionForm, ReplyForm
from .models import Question, Reply

from products.models import Product


class NewQuestionView(FormView):
    model = Question
    template_name = 'questions/question_form.html'
    form_class = QuestionForm

    def form_valid(self, form):
        new_question = form.save(commit=False)
        product = Product.objects.get(pk=self.kwargs['pk'])
        new_question.product = product
        new_question.user = self.request.user
        new_question.save()
        return redirect('product', pk=product.pk)

    def get_context_data(self, **kwargs):
        context = super(NewQuestionView, self).get_context_data(**kwargs)
        product = Product.objects.get(pk=self.kwargs['pk'])
        context['product'] = product
        return context


class NewReplyView(FormView):
    model = Reply
    template_name = 'questions/reply_form.html'
    form_class = ReplyForm

    def form_valid(self, form):
        new_reply = form.save(commit=False)
        question = Question.objects.get(pk=self.kwargs['pk'])
        new_reply.question = question
        new_reply.user = self.request.user
        new_reply.save()
        return redirect('product', pk=question.product.pk)
