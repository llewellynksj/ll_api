from django.urls import path
from leaf import views

urlpatterns = [
  path('leaves/', views.LeafList.as_view()),
]