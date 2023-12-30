from django.urls import path
from quickstart import views

urlpatterns = [
    path('quickstart/', views.snippet_list),
    path('quickstart/<int:pk>/', views.snippet_detail),
]