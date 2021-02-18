from django.urls import path
from . import views

app_name = 'blogapp'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('tag/<slug:tag_slug>/',views.home, name='post_list_by_tag'),
    path('', views.home, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
]