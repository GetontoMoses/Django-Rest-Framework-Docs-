from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from quickstart import views

urlpatterns = [
    path('', views.api_root),
    path('quickstart/<int:pk>/highlight/', views.SnippetHighlight.as_view()),
    path('quickstart/', views.SnippetList.as_view()),
    path('quickstart/<int:pk>/', views.SnippetDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)