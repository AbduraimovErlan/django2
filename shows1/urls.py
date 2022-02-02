
from django.urls import path
from . import views

app_name = 'shows1'
urlpatterns = [
    path('shows1/', views.ShowsListView.as_view(), name='shows_all'),
    path('shows1/<int:id>/', views.ShowsDetailView.as_view(), name='shows_detail'),
    path('shows1/<int:id>/update/', views.ShowsUpdateView.as_view(), name='show_update'),
    path('shows1/<int:id>/delete/', views.ShowsDeleteView.as_view(), name='show_delete'),
    path('add-shows1/', views.ShowsCreateView.as_view(), name='add-shows1'),
]