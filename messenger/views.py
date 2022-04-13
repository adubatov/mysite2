from re import template
from django.shortcuts import render
from django.views import generic

from .models import Message, User

# Create your views here.
class IndexView(generic.ListView):
    model = Message
    template_name = 'messenger/messages.html'
    context_object_name = 'latest_messages'

    def get_queryset(self):
        return Message.objects.order_by('-pub_time')[:10]

class UserView(generic.DetailView):
    model = User
    template_name = 'messenger/user.html'
    context_object_name = 'user'



class NewMessageView(generic.CreateView):
    model = Message
    template_name = 'messenger/new_message.html'
    fields = ['message_text', 'author']


class MessageEditView(generic.UpdateView):
    model = Message
    template_name = 'messenger/message_edit.html'
    fields =['message_text', 'author']


class MessageDetailsView(generic.DetailView):
    model = Message
    template_name = 'messenger/message_details.html'
    context_object_name = 'message'