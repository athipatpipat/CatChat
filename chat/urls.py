from django.urls import path, re_path
from .views import index

app_name = 'chat'

urlpatterns = [

    path('', index, name='chat-home'),

]

