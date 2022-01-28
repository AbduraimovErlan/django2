from django.urls import path
from . import views

app_name = 'parser'
urlpatterns = [
    path('parser/', views.ParserFormView.as_view(), name='parse_func'),
]