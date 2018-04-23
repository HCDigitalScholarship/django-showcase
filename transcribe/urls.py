from django.urls import path

from . import views


urlpatterns = [
    path('<slug>/', views.TextView.as_view(), name='text_detail'),
]
