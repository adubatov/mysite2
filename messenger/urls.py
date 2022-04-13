from django.urls import path

from . import views

app_name = 'messenger'
urlpatterns = [
    path('', views.IndexView.as_view(), name='messages'),
    path('user/<int:pk>', views.UserView.as_view(), name='user'),
    path('message/new', views.NewMessageView.as_view(), name='new_message'),
    path('message/<int:pk>', views.MessageDetailsView.as_view(), name='message_details'),
    path('message/<int:pk>/edit', views.MessageEditView.as_view(), name='message_edit')
]
