from django.urls import path
from . import views

urlpatterns = [
    path('accounts/', views.AccountList.as_view()),
]