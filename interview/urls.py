from django.urls import path
from . import views

app_name = 'interview'

urlpatterns = [
    path('', views.home, name='home'),
    path('interview/<int:role_id>/', views.start_interview, name='start_interview'),
    path('submit_answer/<int:session_id>/', views.submit_answer, name='submit_answer'),
    path('feedback/<int:session_id>/', views.show_feedback, name='show_feedback'),
]
