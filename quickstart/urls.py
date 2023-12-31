from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from quickstart import views

urlpatterns = [
    path('quickstart/', views.SnippetList.as_view()),
    path('quickstart/<int:pk>/', views.SnippetDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)