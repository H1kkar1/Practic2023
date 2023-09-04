from django.urls import path
from . import views
urlpatterns = [
    path('', views.news, name='News'),
    path('create', views.create_post, name='Create_post'),
    path('publication/<number>', views.post, name='Post')
]