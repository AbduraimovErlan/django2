from django.urls import path
from . import views

app_name = 'parser'
urlpatterns = [
    path('parser/', views.ParserFormView.as_view(), name='shows_all_p'),
    path('showss/', views.Shows_p_ListView.as_view(), name='shows_all_p'),
    path('showss/<int:id>/', views.Shows_p_DetailView.as_view(), name='shows_detail_p'),
]