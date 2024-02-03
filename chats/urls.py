from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView

from .views import RegisterView, MessageView

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name="home"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name="register"),
    path('chats/', MessageView.as_view(), name="message")
]