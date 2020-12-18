from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, DeleteView, FormView, ListView

from accounts.models import User
from .models import Message
from .forms import MessageForm


class Messages(ListView):
    model = User
    template_name = 'user-messages/messages.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Messages, self).get_context_data(**kwargs)
        users = []
        sent_messages = Message.objects.filter(sender=self.request.user)
        for message in sent_messages:
            users.append(message.receiver)
        received_messages = Message.objects.filter(receiver=self.request.user)
        for message in received_messages:
            users.append(message.sender)
        users = set(users)

        messages = sent_messages.union(received_messages)
        context['users'] = users
        context['messages'] = messages
        return context


class PrivateMessages(FormView, DetailView):
    model = User
    template_name = 'user-messages/private_messages.html'
    form_class = MessageForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PrivateMessages, self).get_context_data(**kwargs)
        user = User.objects.get(pk=self.kwargs['pk'])
        sent_messages = Message.objects.filter(sender=self.request.user, receiver=user)
        received_messages = Message.objects.filter(receiver=self.request.user, sender=user)
        messages = sent_messages.union(received_messages)
        context['user'] = user
        context['messages'] = messages
        return context

    def form_valid(self, form):
        message = form.save(commit=False)
        message.sender = self.request.user
        message.receiver = User.objects.get(pk=self.kwargs['pk'])
        message.save()
        return redirect('private_messages', pk=message.receiver.pk)


class DeleteMessage(DeleteView):
    model = Message

    def get_success_url(self):
        message = Message.objects.get(pk=self.kwargs['pk'])
        if message.receiver == self.request.user:
            pk = message.sender.pk
        else:
            pk = message.receiver.pk
        return reverse_lazy('private_messages', kwargs={'pk': pk})


def delete_all_messages(request, pk):
    user = User.objects.get(pk=pk)
    sent_messages = Message.objects.filter(sender=user)
    received_messages = Message.objects.filter(receiver=user)
    sent_messages.delete()
    received_messages.delete()
    return redirect('messages')
