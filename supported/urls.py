from django.urls import path
from supported import views

urlpatterns = [
    path('supported/', views.TeamsListView.as_view()),
    path('supported/<int:pk>/', views.TeamsListView.as_view())
]
