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
