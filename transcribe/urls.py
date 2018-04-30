from django.urls import path

from . import views


app_name = 'transcribe'

urlpatterns = [
    path('', views.LandingView.as_view(), name='landing'),
    path('<slug>/', views.text_detail_view, name='text_detail'),
]
