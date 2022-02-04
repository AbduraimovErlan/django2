from django.urls import path
from . import views

app_name = 'parser'
urlpatterns = [
    path('parser/', views.ParserFormView.as_view(), name='shows_all_p'),
    path('parserShows/', views.Shows_p_ListView.as_view(), name='shows_all_p'),
    path('parserShows/<int:id>/', views.Shows_p_DetailView.as_view(), name='shows_detail_p'),
]