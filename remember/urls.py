from django.urls import path
from . import views

urlpatterns = [
  path('remembered/', views.RememberList.as_view(), name='remembered'),
  path('remembered/<int:pk>/', views.RememberDetail.as_view(), name='remembered_detail'),
]