from django.urls import path
from . import views

urlpatterns = [
    path('get_content/', views.GetContent.as_view()),
]