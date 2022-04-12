from django.urls import path

from . import views

app_name = 'messenger'
urlpatterns = [
    path('', views.IndexView.as_view(), name='messages')
]
